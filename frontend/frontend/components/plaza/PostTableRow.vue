<template>
    <div id="post-holder" class="px-5 py-4">
        <div class="flex items-center">
            <div class="flex flex-1 flex-col space-y-1">
                <h2>
                    <NuxtLink
                        :to="postLink"
                        class="font-semibold text-primary hover:underline"
                    >
                        {{ title }}
                    </NuxtLink>
                </h2>
                <p v-if="post" class="flex space-x-1">
                    <span class="text-sm text-gray-700"
                        >By
                        <NuxtLink
                            v-if="includeAuthorLink"
                            :to="authorLink"
                            class="font-semibold hover:underline"
                        >
                            {{ author }}
                        </NuxtLink>
                        <span v-else class="font-semibold">{{
                            author
                        }}</span></span
                    >
                    <span
                        v-if="includePlazaLink"
                        class="text-sm text-gray-700 font-semibold"
                        >&middot;</span
                    >
                    <span v-if="includePlazaLink" class="text-sm text-gray-700"
                        >Posted in
                        <NuxtLink
                            :to="plazaLink"
                            class="font-semibold hover:underline"
                        >
                            {{ plaza }}
                        </NuxtLink></span
                    >
                    <span class="text-sm text-gray-700 font-semibold"
                        >&middot;</span
                    >
                    <span class="text-sm text-gray-700">{{ time }}</span>
                    <span class="text-sm text-gray-700 font-semibold"
                        >&middot;</span
                    >
                    <span class="text-sm text-gray-700">{{
                        last_activity
                    }}</span>
                </p>
            </div>
            <div id="replies" class="flex flex-col w-20">
                <div>
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        class="h-5 w-5 text-secondary mx-auto"
                        viewBox="0 0 20 20"
                        fill="currentColor"
                    >
                        <path
                            fill-rule="evenodd"
                            d="M7.707 3.293a1 1 0 010 1.414L5.414 7H11a7 7 0 017 7v2a1 1 0 11-2 0v-2a5 5 0 00-5-5H5.414l2.293 2.293a1 1 0 11-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z"
                            clip-rule="evenodd"
                        />
                    </svg>
                    <span
                        class="flex text-xs text-gray-500 justify-center mt-1"
                        >{{ replies }}</span
                    >
                </div>
            </div>
            <div id="views" class="sm:flex flex-col w-20 hidden">
                <div>
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        class="h-5 w-5 text-secondary mx-auto"
                        viewBox="0 0 20 20"
                        fill="currentColor"
                    >
                        <path d="M10 12a2 2 0 100-4 2 2 0 000 4z" />
                        <path
                            fill-rule="evenodd"
                            d="M.458 10C1.732 5.943 5.522 3 10 3s8.268 2.943 9.542 7c-1.274 4.057-5.064 7-9.542 7S1.732 14.057.458 10zM14 10a4 4 0 11-8 0 4 4 0 018 0z"
                            clip-rule="evenodd"
                        />
                    </svg>
                    <span
                        class="flex text-xs text-gray-500 justify-center mt-1"
                        >{{ views }}</span
                    >
                </div>
            </div>
        </div>
        <div class="flex flex-wrap mt-2">
            <MiniTag
                v-for="tagged in tags"
                :key="tagged.id"
                :slug="tagged.tag.name"
            />
        </div>
    </div>
</template>

<script>
import MiniTag from '~/components/labels/MiniTag'
export default {
    components: {
        MiniTag,
    },
    props: {
        post: {
            type: Object,
            default: undefined,
        },
        includePlazaLink: {
            type: Boolean,
            default: false,
        },
    },
    data() {
        return {
            rand: Math.ceil(Math.random() * 24) - 1,
        }
    },
    computed: {
        title() {
            return this.post ? this.post.title : '...'
        },
        author() {
            return this.post ? `${this.post.profile.display_name}` : '...'
        },
        includeAuthorLink() {
            return this.post ? !this.post.profile.global_anonymous : false
        },
        authorLink() {
            return this.post ? `/users/${this.post.profile.user}/` : '#'
        },
        plaza() {
            return this.post ? `${this.post.plaza.name}` : '...'
        },
        plazaLink() {
            return this.post ? `/plazas/${this.post.plaza.slug}/` : '#'
        },
        postLink() {
            return this.post
                ? `/plazas/${this.post.plaza.slug}/posts/${this.post.id}/`
                : '#'
        },
        time() {
            if (this.post === undefined) {
                return '...'
            }
            const secondsAgo = Math.floor(
                (new Date() - new Date(this.post.created_at)) / 1000
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
        last_activity() {
            if (this.post === undefined) {
                return '...'
            }
            let secondsAgo
            if (this.post.last_activity == null) {
                secondsAgo = Math.floor(
                    (new Date() - new Date(this.post.created_at)) / 1000
                )
            } else {
                secondsAgo = Math.floor(
                    (new Date() - new Date(this.post.last_activity)) / 1000
                )
            }
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
            return `Last Activity ${time} ${unit}${time === 1 ? '' : 's'} ago`
        },
        views() {
            return this.post ? `${this.post.views} views` : ''
        },
        replies() {
            return this.post ? `${this.post.replies} replies` : ''
        },
        tags() {
            return this.post ? this.post.tags : undefined
        },
    },
}
</script>

<style></style>
