<template>
    <main>
        <div class="container mx-auto">
            <div class="bg-gray-100 px-5 mt-5 mb-5 mx-auto">
                <not-found v-if="plazaNotFound && !loading" id="content" />
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
    </main>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import Pagination from '~/components/helpers/pagination'

export default {
    components: {
        Pagination,
    },
    data() {
        return {
            loading: false,
        }
    },
    head() {
        return {
            title: `${this.plaza.name} | EconPlaza`,
        }
    },
    computed: {
        ...mapGetters({
            plaza: 'plazas/currentPlaza',
            posts: 'plazas/posts/posts',
            pagination: 'plazas/posts/pagination',
        }),
        plazaNotFound() {
            // Determine if plaza exists if the ID is 0 (the undefined plaza)
            return this.plaza && this.plaza.id === 0
        },
    },
    watchQuery: ['page'],
    async created() {
        this.loading = true
        await this.getCurrentPlaza(this.$route.params.plazas)

        let page = Number(this.$route.query.page)

        if (isNaN(page)) {
            page = 1
        }

        await this.getAllPlazaPosts({
            page,
            plazaSlug: this.$route.params.plazas,
        })
        this.loading = false

        this.$nuxt.$on('pagination-next', () => {
            page += 1
            this.$router.replace({
                path: this.$route.path,
                query: { ...this.$route.query, page: this.page },
            })
        })
        this.$nuxt.$on('pagination-previous', () => {
            page -= 1
            this.$router.replace({
                path: this.$route.path,
                query: { ...this.$route.query, page: this.page },
            })
        })
        this.$nuxt.$on('pagination-size', (newSize) => {
            // Store this size
            this.setPaginationSize(newSize)
        })
    },
    beforeDestroy() {
        this.$nuxt.$off('pagination-next')
        this.$nuxt.$off('pagination-previous')
        this.$nuxt.$off('pagination-size')
    },
    methods: {
        ...mapActions({
            getCurrentPlaza: 'plazas/getCurrentPlaza',
            getAllPlazaPosts: 'plazas/posts/getAllPlazaPosts',
            setPaginationSize: 'plazas/posts/setPaginationSize',
        }),
    },
}
</script>
