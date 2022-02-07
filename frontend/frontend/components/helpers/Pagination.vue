<template>
    <div class="flex justify-end">
        <button
            :disabled="!previous"
            class="
                rounded-lg
                mx-1
                py-3
                px-5
                bg-primary
                text-sm text-gray-50
                font-semibold
                flex
                items-center
                disabled:bg-gray-200 disabled:text-gray-500
            "
            @click="$nuxt.$emit('pagination-previous')"
        >
            <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-6 w-6"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
            >
                <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M10 19l-7-7m0 0l7-7m-7 7h18"
                />
            </svg>
        </button>
        <div
            class="
                rounded-lg
                mx-1
                py-3
                px-5
                bg-primary
                text-md text-gray-50
                font-semibold
                flex
                items-center
            "
        >
            Page:
            {{ page }}
        </div>
        <button
            :disabled="!next"
            class="
                rounded-lg
                mx-1
                py-3
                px-5
                bg-primary
                text-sm text-gray-50
                flex
                items-center
                disabled:bg-gray-200 disabled:text-gray-500
            "
            @click="$nuxt.$emit('pagination-next')"
        >
            <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-6 w-6"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
            >
                <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M14 5l7 7m0 0l-7 7m7-7H3"
                />
            </svg>
        </button>
    </div>
</template>

<script>
export default {
    name: 'Pagination',
    props: {
        next: {
            type: String,
            default: null,
        },
        page: {
            type: Number,
            default: 1,
        },
        previous: {
            type: String,
            default: null,
        },
    },
}
</script>
