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
      <voucher-header :first-name="firstName" />
      <Error v-if="error" :message="error" />
      <div class="bg-gray-100 px-4 py-2">
        <form class="space-y-4" @submit.prevent="userLogin">
          <div>
            <strong
              >Are you certain that this name belongs to a real person who you
              know?</strong
            >
            <input v-model="voucher.name" type="checkbox" />
          </div>
          <div>
            <strong
              >Are you 100% certain that this email belongs to the person named
              above?</strong
            >
            <input v-model="voucher.email" type="checkbox" />
          </div>
          <div>
            <strong
              >Are you 100% certain the institutional affiliation and position
              of the person named above are correct?</strong
            >
            <input v-model="voucher.institution" type="checkbox" />
          </div>
          <div v-if="voucher.name && voucher.email && voucher.institution">
            <button
              type="submit"
              class="
                w-full
                py-4
                bg-blue-600
                hover:bg-blue-800
                rounded-r-2xl rounded-b-2xl
                text-m
                font-bold
                border border-blue-600
                text-white
                shadow
                transition
                duration-200
                disabled:bg-gray-100
                disabled:text-gray-500
                disabled:border-gray-400
              "
            >
              Vouch
            </button>
          </div>
        </form>
      </div>
    </ul>
  </div>
</template>

<script>
import VoucherHeader from '~/components/vouch/voucher-header'

export default {
  name: 'VouchBox',
  components: {
    VoucherHeader,
  },
  props: {
    firstName: { type: String, default: null },
    vouches: { type: Array, default: null },
  },
  data() {
    return {
      voucher: {
        name: false,
        email: false,
        institution: false,
        isDisabled: true,
      },
      error: null,
    }
  },
}
</script>

<style></style>
