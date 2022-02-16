<template>
    <main>
        <div class="container mx-auto">
            <div class="bg-gray-100 px-5 mt-5 mb-5 mx-auto">
                <not-found v-if="postNotFound && loaded" id="content" />
                <div v-else id="content" class="flex space-x-5 pt-5 pb-8">
                    <div id="content-left" class="w-full lg:w-3/4">
                        <post-box />
                        <comment-table />
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
                        <post-stat-box />
                        <about-box />
                        <rules-box />
                    </div>
                </div>
            </div>
        </div>
    </main>
</template>

<script>
import { mapMutations } from 'vuex'
import { PLAZAS } from '~/api-routes'
import Pagination from '~/components/helpers/Pagination'

export default {
    components: {
        Pagination,
    },
    async asyncData({ query, params, store }) {
        await store.dispatch('plazas/getCurrentPlaza', {
            plazaSlug: params.plazas,
        })

        // Need to get all the current Plaza posts before we can run current post
        await store.dispatch('plazas/posts/getAllPlazaPosts', {
            page: 1,
            plazaSlug: params.plazas,
        })

        await store.dispatch('plazas/posts/getCurrentPost', {
            plazaSlug: params.plazas,
            postID: params.id,
        })

        let page = Number(query.page)

        if (isNaN(page)) {
            page = 1
        }

        await store.dispatch('plazas/posts/comments/getCurrentPostComments', {
            page,
            plazaSlug: params.plazas,
            postID: params.id,
        })

        return {
            loaded: true,
            page,
            plaza: store.getters['plazas/currentPlaza'],
            post: store.getters['plazas/posts/currentPost'],
            pagination: store.getters['plazas/posts/comments/pagination'],
        }
    },
    data() {
        return {
            loading: false,
        }
    },
    head() {
        return {
            title: `${this.post.title} | ${this.plaza.name} | EconPlaza`,
        }
    },
    computed: {
        postNotFound() {
            // Determine if post exists if the ID is 0 (the undefined post)
            return this.post && this.post.id === 0
        },
    },
    watchQuery: ['page'],
    mounted() {
        this.$axios.post(
            PLAZAS.VIEWPOST(this.$route.params.plazas, this.$route.params.id)
        )
    },
    beforeDestroy() {
        this.$nuxt.$off('pagination-next')
        this.$nuxt.$off('pagination-previous')
        this.$nuxt.$off('pagination-size')
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
    },
    methods: {
        ...mapMutations({
            setDesiredPaginationSize:
                'plazas/posts/comments/setDesiredPaginationSize',
        }),
    },
}
</script>
