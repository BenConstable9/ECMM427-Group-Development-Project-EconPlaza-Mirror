<template>
  <div v-if="isAuthenticated" class="flex items-center space-x-4">
    <div id="profile" class="relative">
      <div
        class="flex items-center space-x-2 cursor-pointer"
        @click="showMenu = !showMenu"
      >
        <div
          id="picture"
          class="rounded-full overflow-hidden ring-2 ring-gray-100"
        >
          <img
            class="select-none object-cover w-8 h-8"
            src="https://placekitten.com/64/64"
          />
        </div>
        <div id="chevron" class="text-gray-100">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-6 w-6"
            viewBox="0 0 20 20"
            fill="currentColor"
          >
            <path
              fill-rule="evenodd"
              d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
              clip-rule="evenodd"
            />
          </svg>
        </div>
      </div>
      <Dropdown v-model="showMenu" />
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import Dropdown from './Dropdown/Dropdown'
export default {
  components: { Dropdown },
  data() {
    return {
      showMenu: false,
    }
  },
  computed: {
    ...mapGetters(['isAuthenticated', 'authenticatedUser']),
  },
}
</script>

<style></style>
