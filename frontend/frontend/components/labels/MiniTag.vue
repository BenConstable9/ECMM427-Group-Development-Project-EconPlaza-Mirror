<template>
    <NuxtLink :to="`/tags/${slug}/`">
        <div
            class="
                px-2
                py-1
                bg-secondary
                rounded-lg
                text-xs text-white
                mr-1
                mb-1
                transition
                hover:bg-primary
            "
        >
            # {{ slug }}
        </div>
    </NuxtLink>
</template>

<script>
export default {
    name: 'MiniTag',
    props: {
        slug: {
            type: String,
            default: '',
        },
    },
}
</script>
