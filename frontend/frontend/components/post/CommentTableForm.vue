<template>
    <div>
        <Error v-if="error" :message="error" />
        <Success v-if="success" :message="success" />
        <div id="post-heading" class="flex space-x-3 items-center px-5 py-3">
            <form class="space-y-4 w-full" @submit.prevent="commentNew">
                <div>
                    Post Comment as:
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
                            rounded-r-2xl rounded-b-2xl
                            text-blue-600
                            shadow
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
                            {{ item.display_name }}
                        </option>
                    </select>
                </div>
                <div>
                    <textarea
                        v-model="comment.content"
                        :disabled="comment.isDisabled"
                        class="
                            w-full
                            p-4
                            text-m
                            bg-white
                            focus:outline-none
                            border border-gray-200
                            rounded-r-2xl rounded-b-2xl
                            text-blue-600
                            shadow
                            disabled:bg-gray-100
                            disabled:text-gray-500
                            disabled:border-gray-400
                        "
                        type="text"
                        placeholder="Post Content"
                        rows="5"
                        maxlength="2800"
                    >
                    </textarea>
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
                            bg-blue-600
                            hover:bg-blue-800
                            rounded-r-2xl rounded-b-2xl
                            text-m
                            font-bold
                            border border-blue-600
                            text-white
                            shadow
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
        }),
    },
    async created() {
        await this.getAllProfiles()
    },
    methods: {
        ...mapActions({
            getCurrentProfile: 'profiles/getCurrentProfile',
            getAllProfiles: 'profiles/getAllProfiles',
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
                    }
                )
                .then((response) => {
                    this.comment.isDisabled = false
                    this.comment.content = ''
                    this.success = 'Comment posted successfully.'
                    this.addComment(response.data)
                    this.increaseReplyCount()
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
