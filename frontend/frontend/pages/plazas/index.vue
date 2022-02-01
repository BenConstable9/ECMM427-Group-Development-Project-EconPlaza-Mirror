<template>
    <main>
        <div class="container mx-auto">
            <div class="bg-gray-50 px-5 mx-auto">
                <div id="title">
                    <div class="flex pt-8">
                        <h1 class="text-xl font-semibold">All Plazas</h1>
                    </div>
                </div>
                <div id="content">
                    <div
                        id="plazas"
                        class="
                            grid
                            sm:grid-cols-2
                            md:grid-cols-3
                            lg:grid-cols-4
                            gap-4
                            my-6
                        "
                    >
                        <NuxtLink
                            v-for="plaza in plazas"
                            :key="plaza.id"
                            :to="`/plazas/${plaza.slug}`"
                        >
                            <plaza-box :plaza="plaza" />
                        </NuxtLink>
                    </div>
                    <pagination
                        :next="pagination.next"
                        :page="pagination.page"
                        :previous="pagination.previous"
                    />
                </div>
            </div>
        </div>
    </main>
</template>

<script>
import Pagination from '~/components/helpers/pagination'

export default {
    components: {
        Pagination,
    },
    async asyncData({ query, params, store }) {
        let page = Number(query.page)

        if (isNaN(page)) {
            page = 1
        }

        let search = query.search

        if (search === undefined) {
            search = ''
        }

        await store.dispatch('plazas/getAllPlazas', {
            page,
            search,
        })

        return {
            plazas: store.getters['plazas/allPlazas'],
            pagination: store.getters['plazas/pagination'],
        }
    },
    data() {
        return {}
    },
    head() {
        return {
            title: 'All Plazas | EconPlaza',
        }
    },
    watchQuery: ['page', 'search'],
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
    },
    beforeDestroy() {
        this.$nuxt.$off('pagination-next')
        this.$nuxt.$off('pagination-previous')
    },
}
</script>

<style></style>
