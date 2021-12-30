<template>
  <div class="bg-gray-200 px-4 py-2">Do you</div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'VouchBoxDetails',
  props: { vouches: { type: Array, default: null } },
  computed: {
    ...mapGetters(['authenticatedUser']),
  },
}
</script>

<style></style>
