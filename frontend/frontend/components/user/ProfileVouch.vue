<template>
    <div id="vouch-container" class="flex items-center justify-between">
        <p class="text-gray-700 py-2">
            {{ vouch.voucher.first_name }} {{ vouch.voucher.last_name }}
        </p>
        <Verified v-if="vouch.voucher.verified" />
    </div>
</template>

<script>
import Verified from '~/components/labels/verified'

export default {
    components: {
        Verified,
    },
    props: {
        vouch: {
            type: Object,
            default: () => {},
        },
    },
}
</script>
