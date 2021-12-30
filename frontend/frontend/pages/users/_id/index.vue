<template>
  <main>
    <div class="container mx-auto">
      <div class="bg-gray-50 px-5 mx-auto">
        <div id="title">
          <div class="flex pt-8">
            <h1 class="text-xl font-semibold">
              {{ user.first_name }} {{ user.last_name }}
            </h1>
            <staff v-if="user.is_staff" class="sm:ml-2" />
            <verified v-if="user.verified" class="sm:ml-2" />
          </div>
        </div>
        <!-- Leave room for future labels etc -->
        <div id="content" class="pt-5 pb-8">
          <div
            class="grid sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-2 my-6"
          >
            <div>
              <ul class="list-none">
                <li>
                  <span class="font-semibold">Username:</span>
                  {{ user.username }}
                </li>
                <li>
                  <span class="font-semibold">Email:</span> {{ user.email }}
                </li>
                <li>
                  <span class="font-semibold">Date Joined:</span>
                  {{ new Date(user.date_joined).getFullYear() }}
                </li>
              </ul>
            </div>
            <vouch-box :first-name="user.first_name" :vouches="vouches" />
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import VouchBox from '~/components/vouch/vouch-box'
import Staff from '~/components/labels/staff'
import Verified from '~/components/labels/verified'

export default {
  components: {
    VouchBox,
    Staff,
    Verified,
  },
  async asyncData({ $axios, params }) {
    try {
      const user = await $axios.$get(`/v1/accounts/users/${params.id}/`)
      try {
        const vouches = await $axios.$get(`/v1/accounts/vouches/${params.id}/`)

        return { user, vouches }
      } catch (e) {
        const vouches = []

        return { user, vouches }
      }
    } catch (e) {
      return { user: [] }
    }
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
  head() {
    return {
      title:
        'View ' +
        this.user.first_name +
        ' ' +
        this.user.last_name +
        ' | EconPlaza',
    }
  },
}
</script>

<style></style>
