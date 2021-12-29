<template>
  <div class="flex flex-row bg-blue-600 px-4 py-2">
    <h3 class="basis-3/4 text-lg font-semibold text-white">
      {{ firstName }} {{ lastName }}
    </h3>
    <staff v-if="isStaff" class="basis-1/4" />
  </div>
</template>

<script>
import Staff from '~/components/labels/staff'

export default {
  name: 'UserBoxHeader',
  components: {
    Staff,
  },
  props: {
    firstName: { type: String, default: '' },
    lastName: { type: String, default: '' },
    isStaff: { type: Boolean, default: false },
  },
}
</script>

<style></style>
