<template>
    <div class="bg-gray-100 px-4 py-2">
        <ul v-if="vouches.length > 0" class="list-none">
            <div
                v-for="vouch in vouches"
                :key="vouch.voucher.id"
                class="flex items-start border-b py-2"
            >
                <div class="flex-1 md:flex-none lg:flex-1">
                    <NuxtLink :to="`/users/${vouch.voucher.id}`">
                        <h4 class="text-md font-semibold text-blue-400">
                            {{ vouch.voucher.first_name }}
                            {{ vouch.voucher.last_name }}
                        </h4>
                    </NuxtLink>
                </div>
                <verified
                    v-if="vouch.voucher.verified"
                    class="flex-initial md:flex-none lg:flex-initial"
                />
                <staff
                    v-if="vouch.voucher.isStaff"
                    class="flex-initial md:flex-none lg:flex-initial"
                />
            </div>
        </ul>
        <div v-else class="py-2">
            <h4 class="text-md font-semibold text-red-400">
                No one has vouched yet!
            </h4>
        </div>
    </div>
</template>

<script>
import Verified from '~/components/labels/verified'
import Staff from '~/components/labels/staff'

export default {
    name: 'VouchBoxDetails',
    components: {
        Verified,
        Staff,
    },
    props: { vouches: { type: Array, default: null } },
}
</script>

<style></style>
