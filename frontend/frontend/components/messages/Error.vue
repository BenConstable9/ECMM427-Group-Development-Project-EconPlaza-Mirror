<template>
    <div
        class="
            w-full
            px-5
            py-3
            bg-red-600
            text-m
            font-bold
            text-white
            flex
            items-center
        "
    >
        <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-6 w-6 inline mr-1"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
        >
            <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
            />
        </svg>
        Error: {{ message }}
    </div>
</template>

<script>
export default {
    name: 'Error',
    props: {
        message: {
            type: String,
            default: '',
        },
    },
}
</script>
