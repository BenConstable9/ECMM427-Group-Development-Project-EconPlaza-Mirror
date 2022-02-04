<template>
    <NuxtLink :to="`/tags/${slug}/`">
        <div
            class="p-3 bg-red-700 rounded-r-xl rounded-b-xl text-xs text-white"
        >
            {{ slug }}
        </div>
    </NuxtLink>
</template>

<script>
export default {
    name: 'Tag',
    props: {
        slug: {
            type: String,
            default: '',
        },
    },
}
</script>
