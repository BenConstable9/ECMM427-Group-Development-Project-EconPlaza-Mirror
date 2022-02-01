<template>
    <div class="flex justify-end">
        <button
            :disabled="!previous"
            class="
                rounded-full
                bg-gray-50
                mx-2
                p-3
                bg-blue-600
                hover:bg-blue-800
                text-sm
                border border-blue-800
                text-white
                shadow
                transition
                duration-200
                flex
                items-center
                disabled:bg-gray-100
                disabled:text-gray-500
                disabled:border-gray-400
            "
            @click="$nuxt.$emit('pagination-previous')"
        >
            <span class="font-bold pr-1">&larr;</span> Previous
        </button>
        <div
            class="
                rounded-full
                bg-gray-50
                mx-2
                p-3
                bg-blue-600
                hover:bg-blue-800
                text-sm
                border border-blue-800
                text-white
                shadow
                transition
                duration-200
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
                rounded-full
                bg-gray-50
                mx-2
                p-3
                bg-blue-600
                hover:bg-blue-800
                text-sm
                border border-blue-800
                text-white
                shadow
                transition
                duration-200
                flex
                items-center
                disabled:bg-gray-100
                disabled:text-gray-500
                disabled:border-gray-400
            "
            @click="$nuxt.$emit('pagination-next')"
        >
            Next
            <span class="font-bold pl-1">&rarr;</span>
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
