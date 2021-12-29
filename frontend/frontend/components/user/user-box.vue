<template>
  <div>
    <ul
      class="
        flex flex-col
        w-full
        border
        rounded-r-2xl rounded-b-2xl
        overflow-hidden
        shadow-md
      "
    >
      <user-box-header
        :first-name="user.first_name"
        :last-name="user.last_name"
        :is-staff="user.is_staff"
      />
      <user-box-details
        :email="user.email"
        :date-joined="new Date(user.date_joined)"
        :verified="user.verified"
      />
    </ul>
  </div>
</template>

<script>
import UserBoxDetails from '~/components/user/user-box-details'
import UserBoxHeader from '~/components/user/user-box-header'

export default {
  name: 'UserBox',
  components: {
    UserBoxDetails,
    UserBoxHeader,
  },
  props: { user: { type: Object, default: null } },
}
</script>

<style></style>
