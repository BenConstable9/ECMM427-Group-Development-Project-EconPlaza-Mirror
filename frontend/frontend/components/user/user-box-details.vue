<template>
  <div class="flex flex-row bg-gray-100 px-4 py-2">
    <div class="basis-3/4">
      <p class="text-base text-gray-900">{{ email }}</p>
      <p class="text-base text-gray-900">
        Joined: {{ months[dateJoined.getMonth()] }},
        {{ dateJoined.getFullYear() }}
      </p>
    </div>
    <verified v-if="verified" class="basis-1/4" />
  </div>
</template>

<script>
import Verified from '~/components/labels/verified'

export default {
  name: 'UserBoxDetails',
  components: {
    Verified,
  },
  props: {
    email: { type: String, default: '' },
    dateJoined: { type: Date, default: '' },
    verified: { type: Boolean, default: false },
  },
  data() {
    return {
      months: [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December',
      ],
    }
  },
}
</script>

<style></style>
