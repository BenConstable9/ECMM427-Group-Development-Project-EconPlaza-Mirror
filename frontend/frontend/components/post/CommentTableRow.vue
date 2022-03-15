<template>
    <div id="comment-info" class="flex items-center px-5 py-4">
        <div class="flex flex-1 flex-col space-y-1">
            <MarkdownViewer :content="content" />
            <div class="flex flex-row border-t py-3 mx-5">
                <p class="flex-1 flex space-x-1 mt-1">
                    <span class="text-xs text-gray-700"
                        >By
                        <NuxtLink
                            v-if="includeAuthorLink"
                            :to="authorLink"
                            class="font-semibold hover:underline"
                        >
                            {{ author }}
                        </NuxtLink>
                        <span v-else class="font-semibold">{{ author }}</span>
                    </span>
                    <span class="text-xs text-gray-700 font-semibold"
                        >&middot;</span
                    >
                    <span class="text-xs text-gray-700">{{ time }}</span>
                </p>
                <div class="flex-initial flex space-x-1 mt-1">
                    <div
                        v-if="
                            authenticatedUser.verified &&
                            plaza.membership.member
                        "
                        class="
                            cursor-pointer
                            rounded
                            transition
                            text-gray-400
                            flex
                            inline-center
                            text-xs
                            hover:text-gray-600
                        "
                        @click="setReply"
                    >
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            class="h-4 w-4 inline mr-1"
                            viewBox="0 0 20 20"
                            fill="currentColor"
                        >
                            <path
                                fill-rule="evenodd"
                                d="M7.707 3.293a1 1 0 010 1.414L5.414 7H11a7 7 0 017 7v2a1 1 0 11-2 0v-2a5 5 0 00-5-5H5.414l2.293 2.293a1 1 0 11-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z"
                                clip-rule="evenodd"
                            />
                        </svg>
                        Reply
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
    props: {
        comment: {
            type: Object,
            default: undefined,
        },
    },
    data() {
        return {
            rand: Math.ceil(Math.random() * 24) - 1,
        }
    },
    computed: {
        ...mapGetters({
            authenticatedUser: 'authenticatedUser',
            plaza: 'plazas/currentPlaza',
        }),
        content() {
            return this.comment ? this.comment.content : '...'
        },
        author() {
            return this.comment ? `${this.comment.profile.display_name}` : '...'
        },
        includeAuthorLink() {
            return this.comment ? !this.comment.profile.global_anonymous : false
        },
        authorLink() {
            return this.comment ? `/users/${this.comment.profile.user}/` : '#'
        },
        time() {
            if (this.comment === undefined) {
                return '...'
            }
            const secondsAgo = Math.floor(
                (new Date() - new Date(this.comment.created_at)) / 1000
            )
            let time = secondsAgo
            let unit = 'second'
            if (secondsAgo > 31536000) {
                time = Math.floor(secondsAgo / 31536000)
                unit = 'year'
            } else if (secondsAgo > 2592000) {
                time = Math.floor(secondsAgo / 2592000)
                unit = 'month'
            } else if (secondsAgo > 604800) {
                time = Math.floor(secondsAgo / 604800)
                unit = 'week'
            } else if (secondsAgo > 86400) {
                time = Math.floor(secondsAgo / 86400)
                unit = 'day'
            } else if (secondsAgo > 3600) {
                time = Math.floor(secondsAgo / 3600)
                unit = 'hour'
            } else if (secondsAgo > 60) {
                time = Math.floor(secondsAgo / 60)
                unit = 'minute'
            }
            return `Posted ${time} ${unit}${time === 1 ? '' : 's'} ago`
        },
    },
    methods: {
        setReply() {
            this.$nuxt.$emit('set-comment-reply', this.comment)
        },
    },
}
</script>

<style></style>
