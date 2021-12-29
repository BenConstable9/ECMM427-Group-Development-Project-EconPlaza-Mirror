<template>
  <main>
    <div class="container mx-auto">
      <div class="bg-gray-50 px-5 mx-auto">
        <div id="title">
          <div class="flex pt-8">
            <h1 class="text-xl font-semibold">All EconPlaza Users</h1>
          </div>
        </div>
        <div id="content" class="grid grid-cols-4 gap-4 my-6">
          <NuxtLink
            v-for="user in users.results"
            :key="user.id"
            :to="`users/${user.id}`"
          >
            <user-box :user="user" />
          </NuxtLink>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import UserBox from '~/components/user/user-box'

export default {
  components: {
    UserBox,
  },
  async asyncData({ $axios, params }) {
    try {
      const users = await $axios.$get(`/v1/accounts/users/`)
      return { users }
    } catch (e) {
      return { users: [] }
    }
  },
  head() {
    return {
      title: 'All Users | EconPlaza',
    }
  },
}
</script>

<style></style>
