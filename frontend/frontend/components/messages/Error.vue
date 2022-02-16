<template>
    <div
        role="alert"
        class="
            bg-red-100
            border-t-4 border-red-500
            text-red-700
            duration-100
            px-3
            py-3
        "
    >
        <div class="flex space-x-3 text-red-500">
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
                    d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                />
            </svg>
            <div id="message">
                <h3 class="text-red-900 font-semibold">Error</h3>
                <p class="text-sm text-red-900">{{ message }}</p>
            </div>
        </div>
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
