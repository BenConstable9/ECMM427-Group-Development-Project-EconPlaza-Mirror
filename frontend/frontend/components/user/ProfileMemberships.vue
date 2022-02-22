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
            {{ memberships }}
        </div>
    </div>
</template>

<script>
import { USERS } from '../../api-routes'

export default {
    data() {
        return {
            memberships: {
                count: 0,
            },
        }
    },
    async fetch() {
        const response = await this.$axios.get(
            USERS.MEMBERSHIPS(this.$route.params.id)
        )
        this.memberships = response.data
    },
}
</script>
