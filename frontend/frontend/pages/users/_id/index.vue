<template>
    <main>
        <div class="container mx-auto">
            <div class="bg-gray-100 px-5 mt-5 mb-5 mx-auto">
                <div id="content" class="space-x-5 pt-5 pb-8">
                    <div
                        class="
                            flex flex-col
                            md:flex-row
                            space-x-0
                            md:space-x-5
                            space-y-5
                            md:space-y-0
                        "
                    >
                        <div
                            id="left-bar"
                            class="w-full md:w-72 flex-col space-y-5"
                        >
                            <ProfileHeader :user="user" />
                            <ProfileVouches :vouches="vouches" />
                            <ProfileMemberships />
                        </div>
                        <div
                            id="right-bar"
                            class="flex-grow flex-col space-y-5"
                        >
                            <ProfileActivity />
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>
</template>

<script>
import { mapGetters } from 'vuex'
import { USERS } from '../../../api-routes'

export default {
    async asyncData({ $axios, params, store }) {
        try {
            const user = await $axios.$get(USERS.ONE(params.id))
            try {
                const vouches = await $axios.$get(USERS.VOUCHES(params.id))

                const alreadyVouched =
                    vouches.filter(
                        (item) =>
                            item.voucher.id ===
                            store.getters.authenticatedUser.id
                    ).length > 0

                const canVouch =
                    store.getters.authenticatedUser.verified &&
                    store.getters.authenticatedUser.id !== Number(params.id) &&
                    !alreadyVouched

                return { user, vouches, canVouch }
            } catch (e) {
                const vouches = []

                return { user, vouches, canVouch: false }
            }
        } catch (e) {
            return { user: [], vouches: [], canVouch: false }
        }
    },
    data() {
        return {
            months: [
                'January',
                'February',
                'March',
                'April',
                'May',
                'June',
                'July',
                'August',
                'September',
                'October',
                'November',
                'December',
            ],
        }
    },
    head() {
        return {
            title:
                'View ' +
                this.user.first_name +
                ' ' +
                this.user.last_name +
                ' | EconPlaza',
        }
    },
    computed: {
        ...mapGetters(['authenticatedUser']),
    },
    created() {
        this.$nuxt.$on('user-vouched', () => {
            // They might now be verified so refresh the data
            this.$nuxt.refresh()
        })
    },
    beforeDestroy() {
        this.$nuxt.$off('user-vouched')
    },
}
</script>

<style></style>
