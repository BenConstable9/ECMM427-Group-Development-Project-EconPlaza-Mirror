<template>
  <div class="flex items-start bg-blue-600 px-4 py-2">
    <h3 class="flex-1 md:flex-none lg:flex-1 text-lg font-semibold text-white">
      Who has vouched for {{ firstName }}?
    </h3>
  </div>
</template>

<script>
export default {
  name: 'VouchBoxHeader',
  props: { firstName: { type: String, default: null } },
}
</script>

<style></style>
