<template>
    <div
        id="rules-info"
        class="flex items-center px-3 py-2"
        style="min-height: 36px"
        :class="{ 'animate-pulse': loading }"
    >
        <NuxtLink v-if="!loading" :to="`/plazas/${plaza.slug}`">
            <li class="text-sm text-gray-900 hover:underline">
                {{ plaza.name }}
            </li>
        </NuxtLink>
    </div>
</template>

<script>
export default {
    name: 'MyPlazaRow',
    props: {
        plaza: {
            type: Object,
            required: true,
        },
        loading: {
            type: Boolean,
            default: false,
        },
    },
}
</script>

<style></style>
