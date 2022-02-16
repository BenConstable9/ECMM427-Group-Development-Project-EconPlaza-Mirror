<template>
    <div id="posts" class="flex">
        <ul class="flex flex-col w-full border rounded-lg overflow-hidden">
            <post-table-header
                :include-plaza-actions="isPlaza"
                :title="title"
                :description="description"
            />
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
                    :include-plaza-link="!isPlaza"
                    :class="{ 'bg-gray-50': index % 2 }"
                />
            </div>
        </ul>
    </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
    props: {
        viewType: { type: String, default: 'plaza' },
        title: { type: String, default: '' },
        description: { type: String, default: '' },
    },
    data() {
        return { page: undefined, loading: true }
    },
    computed: {
        posts() {
            if (this.viewType === 'plaza') {
                return this.$store.getters['plazas/posts/posts']
            } else if (this.viewType === 'post') {
                return this.$store.getters['posts/posts']
            } else {
                return this.$store.getters['tags/posts']
            }
        },
        isPlaza() {
            return this.viewType === 'plaza'
        },
    },
    async created() {
        this.loading = true

        this.page = Number(this.$route.query.page)

        if (isNaN(this.page)) {
            this.page = 1
        }

        if (this.viewType === 'plaza') {
            await this.getAllPlazaPosts({
                page: this.page,
                plazaSlug: this.$route.params.plazas,
            })
        } else if (this.viewType === 'post') {
            let search = this.$route.query.search

            if (search === undefined) {
                search = ''
            }

            await this.getAllPosts({
                page: this.page,
                search,
            })
        } else {
            await this.getTaggedPosts({
                page: this.page,
                tag: this.$route.params.tag,
            })
        }

        this.loading = false
    },
    methods: {
        ...mapActions({
            getAllPlazaPosts: 'plazas/posts/getAllPlazaPosts',
            getAllPosts: 'posts/getAllPosts',
            getTaggedPosts: 'tags/getTaggedPosts',
        }),
    },
}
</script>

<style></style>
