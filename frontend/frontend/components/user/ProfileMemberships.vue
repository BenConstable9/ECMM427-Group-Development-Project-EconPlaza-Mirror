<template>
    <div id="memberships" class="rounded-lg border overflow-hidden">
        <div id="memberships-details" class="flex flex-col justify-center">
            <div
                id="memberships-heading"
                class="flex space-x-3 items-center bg-primary px-5 py-3"
            >
                <div id="title" class="flex-1">
                    <div class="flex flex-col space-y-1">
                        <h1 class="text-gray-50 text-lg font-semibold">
                            Memberships
                        </h1>
                    </div>
                </div>
                <HeaderPagiantion
                    :next="memberships.next"
                    :previous="memberships.previous"
                />
            </div>
            <ol class="list-inside">
                <template v-if="memberships.count == 0">
                    <div
                        id="vouch-container"
                        class="flex items-center px-3 py-2"
                    >
                        <li class="italic px-2 text-sm text-gray-900 py-1">
                            User has no memberships.
                        </li>
                    </div>
                </template>
                <template v-else>
                    <ProfileMembership
                        v-for="(membership, index) in memberships.results"
                        :key="membership.id"
                        :membership="membership"
                        :class="{ 'bg-gray-50': index % 2 }"
                    />
                </template>
            </ol>
        </div>
    </div>
</template>

<script>
import { USERS } from '../../api-routes'
import HeaderPagiantion from '~/components/helpers/HeaderPagiantion'

export default {
    components: {
        HeaderPagiantion,
    },
    data() {
        return {
            page: 1,
            memberships: {
                count: 0,
                next: undefined,
                previous: undefined,
            },
        }
    },
    async fetch() {
        const response = await this.$axios.get(
            USERS.MEMBERSHIPS(this.$route.params.id),
            { params: { page: this.page } }
        )
        this.memberships = response.data
    },
    created() {
        this.$nuxt.$on('header-pagination-next', () => {
            this.page += 1
            this.$fetch()
        })
        this.$nuxt.$on('header-pagination-previous', () => {
            this.page -= 1
            this.$fetch()
        })
    },
    beforeDestroy() {
        this.$nuxt.$off('header-pagination-next')
        this.$nuxt.$off('header-pagination-previous')
    },
}
</script>
