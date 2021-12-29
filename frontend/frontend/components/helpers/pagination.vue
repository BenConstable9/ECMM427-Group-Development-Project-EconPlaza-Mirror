<template>
  <div class="flex justify-end">
    <button
      :disabled="!previous"
      class="
        px-3
        py-1
        mx-2
        my-1
        bg-blue-600
        hover:bg-blue-800
        rounded-2xl
        text-sm
        border border-blue-800
        text-white
        shadow
        transition
        duration-200
        flex
        items-center
        disabled:bg-gray-100 disabled:text-gray-500 disabled:border-gray-400
      "
      @click="$nuxt.$emit('pagination-previous')"
    >
      <span class="font-bold pr-1">&larr;</span> Previous
    </button>
    <button
      :disabled="!next"
      class="
        px-3
        py-1
        mx-2
        my-1
        bg-blue-600
        hover:bg-blue-800
        rounded-2xl
        text-sm
        border border-blue-800
        text-white
        shadow
        transition
        duration-200
        flex
        items-center
        disabled:bg-gray-100 disabled:text-gray-500 disabled:border-gray-400
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
    previous: {
      type: String,
      default: null,
    },
  },
}
</script>
