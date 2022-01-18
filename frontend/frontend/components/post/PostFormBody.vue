<template>
    <div id="post-heading" class="flex space-x-3 items-center px-5 py-3">
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
</template>

<script>
import { PLAZAS } from '../../api-routes'
export default {
    data() {
        return {
            post: {
                title: '',
                content: '',
                isDisabled: false,
            },
            error: null,
        }
    },
    methods: {
        async postNew() {
            this.post.isDisabled = true

            // Send to server
            await this.$axios
                .post(PLAZAS.POSTS(this.$route.params.plazas), {
                    title: this.post.title,
                    content: this.post.content,
                    user: this.$store.getters.authenticatedUser.id,
                })
                .then(this.$nuxt.$emit('user-vouched'))
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
