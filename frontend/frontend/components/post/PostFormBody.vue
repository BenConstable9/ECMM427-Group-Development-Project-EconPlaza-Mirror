<template>
    <div>
        <ul class="w-full bg-gray-50 overflow-hidden">
            <Error v-if="error" :message="error" />
            <div
                id="post-heading"
                class="flex space-x-3 items-center px-5 py-3"
            >
                <form class="space-y-4 w-full" @submit.prevent="postNew">
                    <div>
                        <input
                            v-model="post.title"
                            :disabled="post.isDisabled"
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
                            type="text"
                            placeholder="Post Title"
                            maxlength="140"
                        />
                    </div>
                    <div>
                        Post as:
                        <select
                            :value="profile.id"
                            :disabled="post.isDisabled"
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
                                {{ item.display_name }}
                            </option>
                        </select>
                    </div>
                    <div>
                        <Tags v-model="post.tags" :disabled="post.isDisabled" />
                    </div>
                    <div
                        class="
                            cursor-pointer
                            py-3
                            px-4
                            m-2
                            rounded
                            transition
                            bg-secondary
                            text-gray-50
                        "
                        @click="addTag"
                    >
                        Add Tag
                    </div>
                    {{ search.results }}
                    <div>
                        <Editor
                            v-model="post.content"
                            :disabled="post.isDisabled"
                            placeholder="Type your post here..."
                        />
                    </div>
                    <div
                        v-if="
                            post.title.length > 0 &&
                            post.title.length <= 140 &&
                            post.content.length > 0 &&
                            post.content.length <= 2800
                        "
                    >
                        <button
                            type="submit"
                            :disabled="post.isDisabled"
                            class="
                                w-full
                                py-4
                                bg-primary
                                hover:bg-secondary
                                rounded-lg
                                text-m
                                font-bold
                                text-white
                                shadow
                                transition
                                duration-200
                                disabled:bg-gray-100
                                disabled:text-gray-500
                                disabled:border-gray-400
                            "
                        >
                            Submit Post
                        </button>
                    </div>
                </form>
            </div>
        </ul>
    </div>
</template>

<script>
import { mapGetters, mapActions, mapMutations } from 'vuex'
import { PLAZAS, TAGS } from '../../api-routes'
import Error from '~/components/messages/Error'

export default {
    components: {
        Error,
    },
    data() {
        return {
            search: {
                tag: '',
                results: undefined,
            },
            post: {
                title: '',
                content: '',
                permissions: '{}',
                reactions: '{}',
                tags: [],
                isDisabled: false,
            },
            error: null,
        }
    },
    computed: {
        ...mapGetters({
            profile: 'profiles/currentProfile',
            profiles: 'profiles/allProfiles',
            authenticatedUser: 'authenticatedUser',
            postPagination: 'plazas/posts/pagination',
        }),
    },
    async created() {
        await this.getAllProfiles()
    },
    methods: {
        ...mapActions({
            getCurrentProfile: 'profiles/getCurrentProfile',
            getAllProfiles: 'profiles/getAllProfiles',
            getAllPlazaPosts: 'plazas/posts/getAllPlazaPosts',
            emptyAllPlazaPosts: 'plazas/posts/emptyAllPlazaPosts',
        }),
        ...mapMutations({
            setCurrentProfile: 'profiles/setCurrentProfile',
            increasePostCount: 'plazas/increasePostCount',
        }),
        profileSwitch(e) {
            // Get the profile that matches
            const newProfile = this.profiles.find(
                ({ id }) => id === Number(e.target.value)
            )
            // Update the store
            this.setCurrentProfile(newProfile)
        },
        async addTag() {
            // Send off
        },
        async searchTag() {
            // Send off to server
            await this.$axios
                .get(TAGS.ALL(), {
                    params: {
                        search: this.search.tag,
                    },
                })
                .then(({ data }) => {
                    this.search.results = data.results
                })
        },
        async postNew() {
            this.post.isDisabled = true

            // Send to server
            await this.$axios
                .post(PLAZAS.POSTS(this.$route.params.plazas), {
                    title: this.post.title,
                    content: this.post.content,
                    user: this.$store.getters.authenticatedUser.id,
                    profile: this.profile.id,
                    reactions: this.post.reactions,
                    permissions: this.post.permissions,
                    tags: this.post.tags,
                })
                .then((response) => {
                    // Update post count
                    this.increasePostCount()
                    // Update our previous page we were on so any navigation back to page is fine.
                    this.emptyAllPlazaPosts()
                    // Dispatch the action
                    this.getAllPlazaPosts({
                        page: this.postPagination.page,
                        plazaSlug: this.$route.params.plazas,
                    })
                    this.$router.push(
                        `/plazas/${this.$route.params.plazas}/posts/${response.data.id}/`
                    )
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

                    this.post.isDisabled = false
                })
        },
    },
}
</script>
