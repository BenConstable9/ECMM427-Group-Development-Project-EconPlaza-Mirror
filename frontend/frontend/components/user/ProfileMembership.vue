<template>
    <div id="vouch-container" class="flex items-center px-3 py-2">
        <li class="px-2 text-sm text-gray-900 font-semibold hover:underline">
            <NuxtLink :to="`/plazas/${membership.slug}`"
                >{{ membership.name }}
            </NuxtLink>
        </li>
    </div>
</template>

<script>
export default {
    props: {
        membership: {
            type: Object,
            default: () => {},
        },
    },
}
</script>
