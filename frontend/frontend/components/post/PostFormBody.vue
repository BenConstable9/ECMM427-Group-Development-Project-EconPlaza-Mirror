<template>
    <div>
        <ul
            class="
                w-full
                border
                rounded-r-2xl rounded-b-2xl
                overflow-hidden
                shadow-md
            "
        >
            <Error v-if="error" :message="error" />
            <div
                id="post-heading"
                class="flex space-x-3 items-center px-5 py-3"
            >
                <form class="space-y-4 w-full" @submit.prevent="postNew">
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
                                rounded-r-2xl rounded-b-2xl
                                text-blue-600
                                shadow
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
                        <textarea
                            v-model="post.content"
                            :disabled="post.isDisabled"
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
import { PLAZAS } from '../../api-routes'
import Error from '~/components/messages/Error'
export default {
    components: {
        Error,
    },
    data() {
        return {
            post: {
                title: '',
                content: '',
                permissions: '{}',
                reactions: '{}',
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
        }),
        profileSwitch(e) {
            // Get the profile that matches
            const newProfile = this.profiles.find(
                ({ id }) => id === Number(e.target.value)
            )
            // Update the store
            this.setCurrentProfile(newProfile)
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
                })
                .then((response) => {
                    this.$router.push(
                        `/plazas/${this.$route.params.plazas}/posts/${response.data.id}`
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
