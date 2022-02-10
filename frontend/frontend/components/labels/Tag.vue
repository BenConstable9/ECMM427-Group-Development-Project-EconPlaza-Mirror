<template>
    <NuxtLink :to="`/tags/${slug}/`">
        <div class="py-2 px-3 bg-gray-400 rounded-lg text-xs text-white">
            #{{ slug }}
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
