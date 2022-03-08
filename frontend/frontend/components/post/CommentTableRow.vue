<template>
    <div id="comment-info" class="flex items-center px-5 py-4">
        <div class="flex flex-1 flex-col space-y-1">
            <MarkdownViewer :content="content" />
            <p class="flex space-x-1 mt-1 mx-5 border-t py-3">
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
        </div>
    </div>
</template>

<script>
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
}
</script>

<style></style>
