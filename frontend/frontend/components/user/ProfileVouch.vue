<template>
    <div id="vouch-container" class="flex items-center justify-between">
        <p class="text-gray-700 py-2">Lewis Lloyd</p>
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
