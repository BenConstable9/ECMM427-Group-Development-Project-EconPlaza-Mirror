<template>
    <div id="posts" class="flex">
        <ul class="flex flex-col w-full border rounded-lg overflow-hidden">
            <post-table-header />
            <div v-if="loading">
                <post-table-row
                    v-for="i in 4"
                    :key="i"
                    :class="{ 'bg-gray-50': i % 2 }"
                    class="animate-pulse"
                />
            </div>
            <div v-else>
                <post-table-row
                    v-for="(post, index) in posts"
                    :key="post.id"
                    :post="post"
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
        return { page: undefined, loading: true }
    },
    computed: {
        ...mapGetters({ posts: 'plazas/posts/posts' }),
    },
    async created() {
        this.loading = true

        this.page = Number(this.$route.query.page)

        if (isNaN(this.page)) {
            this.page = 1
        }

        await this.getAllPlazaPosts({
            page: this.page,
            plazaSlug: this.$route.params.plazas,
        })
        this.loading = false
    },
    methods: {
        ...mapActions({ getAllPlazaPosts: 'plazas/posts/getAllPlazaPosts' }),
    },
}
</script>

<style></style>
