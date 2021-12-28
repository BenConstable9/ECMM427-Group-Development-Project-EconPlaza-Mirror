<template>
  <div
    class="
      w-full
      p-4
      bg-red-700
      rounded-r-2xl rounded-b-2xl
      text-m
      font-bold
      text-white
      shadow
    "
  >
    Error: {{ message }}
  </div>
</template>

<script>
export default {
  name: 'Notification',
  props: {
    message: {
      type: String,
      default: '',
    },
  },
}
</script>
