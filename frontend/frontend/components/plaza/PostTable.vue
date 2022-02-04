<template>
    <div id="posts" class="flex">
        <ul class="flex flex-col w-full border rounded-lg overflow-hidden">
            <post-table-header :is-plaza-view="isPlazaView" />
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
                    :include-plaza="!isPlazaView"
                    :class="{ 'bg-gray-50': index % 2 }"
                />
            </div>
        </ul>
    </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
    props: { isPlazaView: { type: Boolean, default: true } },
    data() {
        return { page: undefined, loading: true }
    },
    computed: {
        posts() {
            if (this.isPlazaView) {
                return this.$store.getters['plazas/posts/posts']
            } else {
                return this.$store.getters['posts/posts']
            }
        },
    },
    async created() {
        this.loading = true

        this.page = Number(this.$route.query.page)

        if (isNaN(this.page)) {
            this.page = 1
        }

        if (this.isPlazaView) {
            await this.getAllPlazaPosts({
                page: this.page,
                plazaSlug: this.$route.params.plazas,
            })
        } else {
            let search = this.$route.query.search

            if (search === undefined) {
                search = ''
            }

            await this.getAllPosts({
                page: this.page,
                search,
            })
        }

        this.loading = false
    },
    methods: {
        ...mapActions({ getAllPlazaPosts: 'plazas/posts/getAllPlazaPosts' }),
        ...mapActions({ getAllPosts: 'posts/getAllPosts' }),
    },
}
</script>

<style></style>
