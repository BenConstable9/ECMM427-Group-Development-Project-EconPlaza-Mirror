<template>
  <li
    class="
      text-sm text-gray-900
      bg-gray-50
      hover:bg-gray-100
      cursor-pointer
      border
      rounded-full
      overflow-hidden
      px-3
      py-0.5
    "
  >
    {{ plazaName }}
  </li>
</template>

<script>
export default {
  props: {
    plazaName: { type: String, default: 'Plaza' },
  },
}
</script>

<style></style>
