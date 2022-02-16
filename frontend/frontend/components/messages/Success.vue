<template>
    <div
        role="alert"
        class="
            bg-green-100
            border-t-4 border-green-500
            text-green-700
            duration-100
            px-3
            py-3
        "
    >
        <div class="flex space-x-3 text-green-500">
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
                    d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
                />
            </svg>
            <div id="message">
                <h3 class="text-green-900 font-semibold">Success</h3>
                <p class="text-sm text-green-900">{{ message }}</p>
            </div>
        </div>
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
