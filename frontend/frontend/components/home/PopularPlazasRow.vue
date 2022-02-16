<template>
    <div id="rules-info" class="flex items-center px-3 py-2">
        <li class="text-sm text-gray-900 font-semibold hover:underline">
            <NuxtLink :to="`/plazas/${slug}`">{{ name }} </NuxtLink>
        </li>
    </div>
</template>

<script>
export default {
    props: {
        name: {
            type: String,
            default: 'General',
        },
        slug: {
            type: String,
            default: 'general',
        },
    },
}
</script>

<style></style>
