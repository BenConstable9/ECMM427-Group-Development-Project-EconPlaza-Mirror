<template>
    <main>
        <div class="container mx-auto">
            <div class="bg-gray-100 px-5 mt-5 mb-5 mx-auto">
                <not-found v-if="plazaNotFound && loaded" id="content" />
                <div v-else id="content" class="flex space-x-5 pt-5 pb-8">
                    <div id="content-left" class="w-full lg:w-3/4">
                        <post-table />
                        <pagination
                            :next="pagination.next"
                            :previous="pagination.previous"
                        />
                    </div>
                    <div
                        id="content-left"
                        class="hidden lg:flex lg:w-1/4 flex-col space-y-5"
                    >
                        <about-box />
                        <rules-box />
                    </div>
                </div>
            </div>
        </div>
        {{ plaza }}
    </main>
</template>

<script>
import { mapMutations } from 'vuex'
import Pagination from '~/components/helpers/pagination'

export default {
    components: {
        Pagination,
    },
    async asyncData({ query, params, store }) {
        await store.dispatch('plazas/getCurrentPlaza', {
            plazaSlug: params.plazas,
        })

        let page = Number(query.page)

        if (isNaN(page)) {
            page = 1
        }

        await store.dispatch('plazas/posts/getAllPlazaPosts', {
            page,
            plazaSlug: params.plazas,
        })

        return {
            loaded: true,
            plaza: store.getters['plazas/currentPlaza'],
            pagination: store.getters['plazas/posts/pagination'],
        }
    },
    head() {
        return {
            title: `${this.plaza.name} | EconPlaza`,
        }
    },
    computed: {
        plazaNotFound() {
            // Determine if plaza exists if the ID is 0 (the undefined plaza)
            return this.plaza && this.plaza.id === 0
        },
    },
    watchQuery: ['page'],
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
            this.$nuxt.refresh()
        })
    },
    methods: {
        ...mapMutations({
            setDesiredPaginationSize: 'plazas/posts/setDesiredPaginationSize',
        }),
    },
}
</script>
