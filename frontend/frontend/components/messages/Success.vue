<template>
    <div class="w-full px-5 py-3 bg-green-600 text-m font-bold text-white">
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
                d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
            />
        </svg>
        Success: {{ message }}
    </div>
</template>

<script>
export default {
    name: 'Success',
    props: {
        message: {
            type: String,
            default: '',
        },
    },
}
</script>
