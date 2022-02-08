<template>
    <main>
        <div class="container mx-auto">
            <div class="bg-gray-50 px-5 mx-auto">
                <div id="title">
                    <div class="flex pt-8">
                        <h1 class="text-xl font-semibold">
                            All EconPlaza Users
                        </h1>
                    </div>
                </div>
                <div id="content">
                    <div
                        id="users"
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
                            v-for="user in users.results"
                            :key="user.id"
                            :to="`/users/${user.id}`"
                        >
                            <user-box :user="user" />
                        </NuxtLink>
                    </div>
                    <pagination
                        :next="users.next"
                        :page="page"
                        :previous="users.previous"
                    />
                </div>
            </div>
        </div>
    </main>
</template>

<script>
import { USERS } from '../../api-routes'
import UserBox from '~/components/user/user-box'
import Pagination from '~/components/helpers/Pagination'

export default {
    components: {
        UserBox,
        Pagination,
    },
    async asyncData({ $axios, query }) {
        try {
            let page = Number(query.page)

            if (isNaN(page)) {
                page = 1
            }

            let search = query.search

            if (search === undefined) {
                search = ''
            }

            const users = await $axios.$get(USERS.ALL(), {
                params: {
                    page,
                    search,
                },
            })
            return { users, page }
        } catch (e) {
            return { users: [], page: 1 }
        }
    },
    data() {
        return {}
    },
    head() {
        return {
            title: 'All Users | EconPlaza',
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
