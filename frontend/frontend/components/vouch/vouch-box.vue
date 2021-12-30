<template>
  <div>
    <ul
      class="
        w-full
        border
        rounded-r-2xl rounded-b-2xl
        overflow-hidden
        shadow-md
      "
    >
      <vouch-box-header :first-name="firstName" />
      <vouch-box-details :vouches="vouches" />
      <vouch-box-verify
        v-if="authenticatedUser.is_staff || authenticatedUser.verified"
        :vouches="vouches"
      />
    </ul>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

import VouchBoxDetails from '~/components/vouch/vouch-box-details'
import VouchBoxHeader from '~/components/vouch/vouch-box-header'
import VouchBoxVerify from '~/components/vouch/vouch-box-verify'

export default {
  name: 'VouchBox',
  components: {
    VouchBoxDetails,
    VouchBoxHeader,
    VouchBoxVerify,
  },
  props: {
    firstName: { type: String, default: null },
    vouches: { type: Array, default: null },
  },
  computed: {
    ...mapGetters(['authenticatedUser']),
  },
}
</script>

<style></style>
