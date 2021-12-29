<template>
  <header>
    <nav id="navbar" class="bg-blue-100">
      <div class="container mx-auto px-5">
        <div id="links" class="flex items-center space-x-8 py-3">
          <ul class="flex flex-1">
            <li class="text-xl text-gray-900">
              <nuxt-link to="/">EconPlaza</nuxt-link>
            </li>
          </ul>
          <NuxtLink :to="`users`">All Users</NuxtLink>
          <div v-if="isAuthenticated">
            {{ authenticatedUser.email }}
            <a href="" @click="$auth.logout()">Logout</a>
          </div>
        </div>
      </div>
    </nav>
    <nav id="plazas" class="bg-blue-50">
      <div class="container mx-auto px-5">
        <div id="links" class="flex space-x-8 py-2">
          <ul class="flex flex-1 space-x-2">
            <header-plaza-button plazaName="Home" />
            <header-plaza-button plazaName="General" />
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
import { mapGetters } from 'vuex'
import HeaderPlazaButton from './HeaderPlazaButton.vue'
export default {
  components: { HeaderPlazaButton },
  computed: {
    ...mapGetters(['isAuthenticated', 'authenticatedUser']),
  },
}
</script>

<style></style>
