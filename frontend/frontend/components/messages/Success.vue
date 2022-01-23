<template>
    <div
        class="
            w-full
            p-4
            bg-green-700
            rounded-r-2xl rounded-b-2xl
            text-m
            font-bold
            text-white
            shadow
        "
    >
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
