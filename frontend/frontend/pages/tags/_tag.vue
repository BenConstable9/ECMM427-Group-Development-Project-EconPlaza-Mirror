<template>
    <main>
        <div class="container mx-auto">
            <div class="bg-gray-100 px-5 mb-5 mx-auto">
                <div id="content" class="flex space-x-5 pt-5 pb-8">
                    <div id="content-left" class="w-full lg:w-3/4">
                        <post-table
                            view-type="tag"
                            :title="title"
                            description="Posts across all plazas with these tags"
                        />
                        <pagination
                            :next="pagination.next"
                            :page="pagination.page"
                            :previous="pagination.previous"
                            class="mt-5"
                        />
                    </div>
                    <div
                        id="content-left"
                        class="hidden lg:flex lg:w-1/4 flex-col space-y-5"
                    >
                        <my-plazas />
                        <my-bookmarks />
                        <popular-plazas />
                    </div>
                </div>
            </div>
        </div>
    </main>
</template>

<script>
import { mapMutations } from 'vuex'
import Pagination from '~/components/helpers/Pagination'

export default {
    components: {
        Pagination,
    },
    async asyncData({ query, params, store }) {
        let page = Number(query.page)

        if (isNaN(page)) {
            page = 1
        }

        await store.dispatch('tags/getTaggedPosts', {
            page,
            tag: params.tag,
        })

        return {
            loaded: true,
            page,
            pagination: store.getters['tags/pagination'],
        }
    },
    head() {
        return {
            title: `Tag: #${this.$route.params.tag}`,
        }
    },
    computed: {
        title() {
            return `Posts with Tag: #${this.$route.params.tag}`
        },
    },
    watchQuery: ['page'],
    beforeDestroy() {
        this.$nuxt.$off('pagination-next')
        this.$nuxt.$off('pagination-previous')
        this.$nuxt.$off('pagination-size')
        this.$nuxt.$off('pagination-sort')
    },
    created() {
        this.$nuxt.$on('pagination-next', () => {
            this.page += 1
            this.$router.replace({
                path: this.$route.path,
                query: { ...this.$route.query, page: this.page },
            })
        })
        this.$nuxt.$on('pagination-previous', () => {
            this.page -= 1
            this.$router.replace({
                path: this.$route.path,
                query: { ...this.$route.query, page: this.page },
            })
        })
        this.$nuxt.$on('pagination-size', (newSize) => {
            // Store this size
            this.setDesiredPaginationSize(Number(newSize))

            // If we are already on page 1 then refresh otherwise change page
            if (this.page === 1) {
                this.$nuxt.refresh()
            } else {
                this.page = 1
                this.$router.replace({
                    path: this.$route.path,
                    query: { ...this.$route.query, page: this.page },
                })
            }
        })
        this.$nuxt.$on('pagination-sort', (sort) => {
            // Store this size
            this.setDesiredPaginationSort(sort)

            // If we are already on page 1 then refresh otherwise change page
            if (this.page === 1) {
                this.$nuxt.refresh()
            } else {
                this.page = 1
                this.$router.replace({
                    path: this.$route.path,
                    query: { ...this.$route.query, page: this.page },
                })
            }
        })
    },
    methods: {
        ...mapMutations({
            setDesiredPaginationSize: 'tags/setDesiredPaginationSize',
            setDesiredPaginationSort: 'tags/setDesiredPaginationSort',
        }),
    },
}
</script>
