<template>
    <div id="comments" class="flex">
        <ul class="flex flex-col w-full border rounded-lg overflow-hidden">
            <comment-table-header />
            <comment-table-form v-if="authenticatedUser.verified" />
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
            comments: 'plazas/posts/comments/comments',
            authenticatedUser: 'authenticatedUser',
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
            getCurrentPostComments:
                'plazas/posts/comments/getCurrentPostComments',
        }),
    },
}
</script>

<style></style>
