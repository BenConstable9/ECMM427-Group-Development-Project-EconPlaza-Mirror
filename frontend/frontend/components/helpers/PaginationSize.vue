<template>
    <div class="flex justify-end">
        <select
            :value="size"
            class="rounded-full bg-gray-50 p-3 text-primary"
            @change="$nuxt.$emit('pagination-size', $event.target.value)"
        >
            <option value="5">5</option>
            <option value="10">10</option>
            <option value="20">20</option>
            <option value="50">50</option>
        </select>
    </div>
</template>

<script>
export default {
    name: 'PaginationSize',
    props: {
        size: {
            type: Number,
            default: 10,
        },
    },
    data() {
        return {
            selected: this.size,
        }
    },
}
</script>
