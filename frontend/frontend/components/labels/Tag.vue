<template>
    <NuxtLink :to="`/tags/${slug}/`">
        <div
            class="
                flex
                items-center
                py-1
                px-2
                border border-gray-50
                rounded-lg
                text-sm text-gray-50
                mr-1
                mb-1
                hover:bg-secondary hover:border-secondary
                transition
            "
        >
            <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-4 w-4 inline"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
            >
                <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M7 20l4-16m2 16l4-16M6 9h14M4 15h14"
                />
            </svg>
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
