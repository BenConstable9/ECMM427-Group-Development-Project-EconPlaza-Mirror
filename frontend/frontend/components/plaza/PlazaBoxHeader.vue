<template>
    <div class="flex items-start bg-blue-600 px-4 py-2">
        <h3
            class="
                flex-1
                md:flex-none
                lg:flex-1
                text-lg
                font-semibold
                text-white
            "
        >
            {{ name }}
        </h3>
    </div>
</template>

<script>
export default {
    name: 'PlazaBoxHeader',
    props: {
        name: { type: String, default: '' },
    },
}
</script>

<style></style>
