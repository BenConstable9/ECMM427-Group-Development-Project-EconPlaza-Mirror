<template>
  <div
    class="
      w-full
      px-5
      py-1
      text-sm text-gray-600
      font-semibold
      bg-gray-100
      select-none
    "
  >
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: 'DropdownTitle',
}
</script>
