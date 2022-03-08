<template>
    <div id="comments" class="flex">
        <ul class="flex flex-col w-full border rounded-lg overflow-hidden">
            <comment-table-header />
            <div v-if="loading">
                <comment-table-row
                    v-for="i in 4"
                    :key="i"
                    :class="{ 'bg-gray-50': i % 2 }"
                    class="animate-pulse"
                />
            </div>
            <div v-else>
                <comment-table-row
                    v-for="(comment, index) in comments"
                    :key="comment.id"
                    :comment="comment"
                    :class="{ 'bg-gray-50': index % 2 }"
                />
            </div>
            <comment-table-form
                v-if="authenticatedUser.verified && plaza.membership.member"
                class="bg-gray-50 border-t"
            />
            <div
                v-else
                class="
                    border-t
                    flex
                    text-gray-500
                    h-20
                    justify-center
                    items-center
                    bg-gray-50
                "
            >
                {{
                    authenticatedUser.verified
                        ? "You can't add comments because you have not joined this plaza."
                        : "You can't add comments because you have not been verified."
                }}
            </div>
        </ul>
    </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
    data() {
        return {
            page: undefined,
            loading: false,
        }
    },
    computed: {
        ...mapGetters({
            authenticatedUser: 'authenticatedUser',
            comments: 'plazas/posts/comments/comments',
            plaza: 'plazas/currentPlaza',
        }),
    },
    async created() {
        this.loading = true

        this.page = Number(this.$route.query.page)

        if (isNaN(this.page)) {
            this.page = 1
        }

        await this.getCurrentPostComments({
            page: this.page,
            plazaSlug: this.$route.params.plazas,
            postID: this.$route.params.id,
        })
        this.loading = false
    },
    methods: {
        ...mapActions({
            getCurrentPlaza: 'plazas/getCurrentPlaza',
            getCurrentPostComments:
                'plazas/posts/comments/getCurrentPostComments',
        }),
    },
}
</script>

<style></style>
