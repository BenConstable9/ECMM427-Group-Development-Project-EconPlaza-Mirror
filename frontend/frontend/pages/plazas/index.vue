<template>
    <main>
        <div class="container mx-auto">
            <div class="bg-gray-100 px-5 mt-5 mb-5 mx-auto">
                <div id="title">
                    <div class="flex pt-8">
                        <h1
                            class="
                                text-xl text-gray-900
                                font-semibold
                                flex-grow
                            "
                        >
                            Open Plazas
                        </h1>
                        <NuxtLink
                            v-if="authenticatedUser.verified"
                            :to="`/create/`"
                        >
                            <div
                                class="
                                    rounded-lg
                                    py-2
                                    px-4
                                    bg-primary
                                    text-sm text-gray-50
                                    font-semibold
                                    flex
                                    items-center
                                "
                            >
                                Create Plaza
                            </div>
                        </NuxtLink>
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
                            gap-5
                            pt-5
                            pb-5
                        "
                    >
                        <plaza-box
                            v-for="plaza in plazas"
                            :key="plaza.id"
                            :plaza="plaza"
                        />
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
import { mapGetters } from 'vuex'
import Pagination from '~/components/helpers/Pagination'

export default {
    components: {
        Pagination,
    },
    async asyncData({ query, store }) {
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
            page,
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
    computed: {
        ...mapGetters({
            authenticatedUser: 'authenticatedUser',
        }),
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
