<template>
    <div
        class="
            flex
            items-center
            space-x-2
            w-full
            hover:bg-gray-100
            px-5
            py-3
            text-gray-700
            select-none
        "
        v-on="$listeners"
    >
        <slot></slot>
    </div>
</template>

<script>
export default {
    name: 'DropdownItem',
}
</script>

<style scoped></style>
