<template>
    <div>
        <Error v-if="error" :message="error" />
        <Success v-if="success" :message="success" />
        <div id="post-heading" class="flex space-x-3 items-center px-5 py-3">
            <form
                id="comment-form"
                class="space-y-4 w-full"
                @submit.prevent="commentNew"
            >
                <div
                    v-if="comment.reply"
                    class="
                        w-full
                        bg-white
                        border border-gray-200
                        rounded-lg
                        overflow-hidden
                    "
                >
                    <div
                        class="flex flex-row border-b-2 bg-gray-50 items-center"
                    >
                        <div class="py-3 px-4 m-2 mr-0 flex-grow text-l">
                            Responding to: {{ comment.replyProfile }}
                        </div>
                        <div
                            class="
                                cursor-pointer
                                py-3
                                px-4
                                mx-2
                                rounded
                                transition
                                bg-primary
                                text-gray-50
                            "
                            @click="comment.reply = null"
                        >
                            Remove Response
                        </div>
                    </div>
                    <MarkdownViewer :content="comment.replyContent" />
                </div>
                <div>
                    <Editor
                        v-model="comment.content"
                        :disabled="comment.isDisabled"
                        title="Add Your Reply"
                        placeholder="Type your reply here..."
                    />
                </div>
                <div>
                    <select
                        :value="profile.id"
                        :disabled="comment.isDisabled"
                        class="
                            w-full
                            p-4
                            text-m
                            bg-white
                            focus:outline-none
                            border border-gray-200
                            rounded-lg
                            text-primary
                            disabled:bg-gray-100
                            disabled:text-gray-500
                            disabled:border-gray-400
                        "
                        @change="profileSwitch($event)"
                    >
                        <option
                            v-for="item in profiles"
                            :key="item.id"
                            :value="item.id"
                        >
                            Commenting As: {{ item.display_name }}
                        </option>
                    </select>
                </div>
                <div
                    v-if="
                        comment.content.length > 0 &&
                        comment.content.length <= 2800
                    "
                >
                    <button
                        type="submit"
                        :disabled="comment.isDisabled"
                        class="
                            w-full
                            py-4
                            bg-primary
                            hover:bg-secondary
                            rounded-lg
                            text-m
                            font-bold
                            text-white
                            transition
                            duration-200
                            disabled:bg-gray-100
                            disabled:text-gray-500
                            disabled:border-gray-400
                        "
                    >
                        Submit Comment
                    </button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import { mapGetters, mapActions, mapMutations } from 'vuex'
import { PLAZAS } from '../../api-routes'
import Error from '~/components/messages/Error'
import Success from '~/components/messages/Success'

export default {
    components: {
        Error,
        Success,
    },
    data() {
        return {
            comment: {
                reply: null,
                replyContent: '',
                replyProfile: '',
                content: '',
                reactions: '{}',
                isDisabled: false,
            },
            error: null,
            success: null,
        }
    },
    computed: {
        ...mapGetters({
            profile: 'profiles/currentProfile',
            profiles: 'profiles/allProfiles',
            authenticatedUser: 'authenticatedUser',
            commentPagination: 'plazas/posts/comments/pagination',
        }),
    },
    beforeDestroy() {
        this.$nuxt.$off('set-comment-reply')
    },
    async created() {
        await this.getAllProfiles()
        this.$nuxt.$on('set-comment-reply', (comment) => {
            this.comment.reply = comment.id
            this.comment.replyContent = '> ' + comment.content
            this.comment.replyProfile = comment.profile.display_name
            // Scroll box into view
            const el = this.$el.querySelector('#comment-form')
            if (el) {
                el.scrollIntoView()
            }
        })
    },
    methods: {
        ...mapActions({
            getCurrentProfile: 'profiles/getCurrentProfile',
            getAllProfiles: 'profiles/getAllProfiles',
            emptyAllPostComments: 'plazas/posts/comments/emptyAllPostComments',
            getCurrentPostComments:
                'plazas/posts/comments/getCurrentPostComments',
        }),
        ...mapMutations({
            setCurrentProfile: 'profiles/setCurrentProfile',
            addComment: 'plazas/posts/comments/addComment',
            increaseReplyCount: 'plazas/posts/increaseReplyCount',
        }),
        profileSwitch(e) {
            // Get the profile that matches
            const newProfile = this.profiles.find(
                ({ id }) => id === Number(e.target.value)
            )
            // Update the store
            this.setCurrentProfile(newProfile)
        },
        async commentNew() {
            this.comment.isDisabled = true

            // Send to server
            await this.$axios
                .post(
                    PLAZAS.COMMENTS(
                        this.$route.params.plazas,
                        this.$route.params.id
                    ),
                    {
                        content: this.comment.content,
                        user: this.$store.getters.authenticatedUser.id,
                        profile: this.profile.id,
                        reactions: this.comment.reactions,
                        parent: this.comment.reply,
                    }
                )
                .then(() => {
                    this.comment.isDisabled = false
                    this.comment.content = ''
                    this.success = 'Comment posted successfully.'
                    this.emptyAllPostComments()
                    // Refresh the comment data
                    this.getCurrentPostComments({
                        page: this.commentPagination.page,
                        plazaSlug: this.$route.params.plazas,
                        postID: this.$route.params.id,
                    })
                    this.increaseReplyCount()
                    // Make sure we wipe the stored reply
                    this.comment.reply = null
                    this.comment.replyContent = ''
                    this.comment.replyProfile = ''
                })
                .catch((response) => {
                    if (
                        typeof response === 'string' ||
                        response instanceof String
                    ) {
                        this.error = response
                    } else if ('detail' in response) {
                        this.error = response.detail
                    } else {
                        this.error = 'Unable to process request.'
                    }

                    this.comment.isDisabled = false
                })
        },
    },
}
</script>
