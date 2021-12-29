<template>
  <main>
    <div class="container mx-auto">
      <div class="bg-gray-50 px-5 mx-auto">
        <div id="title">
          <div class="flex pt-8">
            <h1 class="text-xl font-semibold">
              {{ user.first_name }} {{ user.last_name }}
            </h1>
          </div>
        </div>
        <div id="content" class="flex pt-5 pb-8">
          {{ user.email }}
        </div>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  async asyncData({ $axios, params }) {
    try {
      const user = await $axios.$get(`/v1/accounts/users/${params.id}/`)
      return { user }
    } catch (e) {
      return { user: [] }
    }
  },
  head() {
    return {
      title: 'View User | EconPlaza',
    }
  },
}
</script>

<style></style>
