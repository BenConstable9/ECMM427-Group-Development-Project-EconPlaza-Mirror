<template>
    <div class="text-sm text-gray-700 truncate bg-gray-50 px-5 py-4">
        {{ description }}
    </div>
</template>

<script>
export default {
    name: 'PlazaBoxDetails',
    props: {
        description: { type: String, default: '' },
    },
}
</script>

<style></style>
