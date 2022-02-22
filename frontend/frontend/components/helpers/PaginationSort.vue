<template>
    <div class="flex justify-end">
        <select
            :value="sort"
            class="rounded-full bg-gray-50 p-3 text-primary"
            @change="$nuxt.$emit('pagination-sort', $event.target.value)"
        >
            <option v-for="item in options" :key="item.key" :value="item.key">
                {{ item.name }}
            </option>
        </select>
    </div>
</template>

<script>
export default {
    name: 'PaginationSort',
    props: {
        sort: {
            type: String,
            default: 'id',
        },
        options: {
            type: Array,
            default: () => [],
        },
    },
    data() {
        return {
            selected: this.size,
        }
    },
}
</script>
