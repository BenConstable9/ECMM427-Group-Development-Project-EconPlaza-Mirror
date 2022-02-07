<template>
    <div class="h-20 truncate bg-gray-50 px-5 py-3">
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
