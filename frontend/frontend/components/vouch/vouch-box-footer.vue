<template>
    <div class="bg-gray-200 px-4 py-2">
        Total Vouches: <span>{{ vouches.length }}</span>
    </div>
</template>

<script>
export default {
    name: 'VouchBoxDetails',
    props: { vouches: { type: Array, default: null } },
}
</script>

<style></style>
