<template>
  <div v-if="isAuthenticated" class="flex items-center space-x-4">
    <div
      class="absolute top-0 right-0 z-10 h-full w-full bg-black transition"
      :class="{
        'invisible opacity-0': !showMenu,
        'visible opacity-20': showMenu,
      }"
      @click="showMenu = !showMenu"
    ></div>
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
      <div
        id="dropdown"
        class="absolute w-52 right-0 top-10 z-20 transition transform"
        :class="{
          'pointer-events-none opacity-0 -translate-y-1 translate-x-2 scale-95':
            !showMenu,
          'pointer-events-auto opacity-100 translate-y-0 translate-x-0 scale-100':
            showMenu,
        }"
      >
        <div class="bg-gray-50 rounded border shadow">
          <div
            class="
              w-full
              px-5
              py-1
              text-sm text-gray-600
              font-semibold
              bg-gray-100
              select-none
            "
          >
            Account
          </div>
          <NuxtLink :to="`/users/${authenticatedUser.id}`">
            <div
              class="
                flex
                items-center
                space-x-2
                w-full
                hover:bg-gray-100
                px-5
                py-3
                text-gray-700
                select-none
              "
              @click="showMenu = !showMenu"
            >
              <span
                ><svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                >
                  <path
                    fill-rule="evenodd"
                    d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z"
                    clip-rule="evenodd"
                  />
                </svg>
              </span>
              <span>Profile</span>
            </div>
          </NuxtLink>
          <div
            class="
              w-full
              px-5
              py-1
              text-sm text-gray-600
              font-semibold
              bg-gray-100
              select-none
            "
          >
            Plazas
          </div>
          <a href="#">
            <div
              class="
                flex
                items-center
                space-x-2
                w-full
                hover:bg-gray-100
                px-5
                py-3
                text-gray-700
                select-none
              "
              @click="showMenu = !showMenu"
            >
              <span
                ><svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                >
                  <path
                    d="M5 3a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2V5a2 2 0 00-2-2H5zM5 11a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2v-2a2 2 0 00-2-2H5zM11 5a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V5zM14 11a1 1 0 011 1v1h1a1 1 0 110 2h-1v1a1 1 0 11-2 0v-1h-1a1 1 0 110-2h1v-1a1 1 0 011-1z"
                  />
                </svg>
              </span>
              <span>Create a plaza</span>
            </div>
          </a>
          <div
            class="
              w-full
              px-5
              py-1
              text-sm text-gray-600
              font-semibold
              bg-gray-100
              select-none
            "
          >
            Settings
          </div>
          <a href="#" @click="$auth.logout()">
            <div
              class="
                flex
                items-center
                space-x-2
                w-full
                hover:bg-gray-100
                px-5
                py-3
                text-gray-700
                select-none
              "
              @click="showMenu = !showMenu"
            >
              <span
                ><svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                >
                  <path
                    fill-rule="evenodd"
                    d="M3 3a1 1 0 00-1 1v12a1 1 0 102 0V4a1 1 0 00-1-1zm10.293 9.293a1 1 0 001.414 1.414l3-3a1 1 0 000-1.414l-3-3a1 1 0 10-1.414 1.414L14.586 9H7a1 1 0 100 2h7.586l-1.293 1.293z"
                    clip-rule="evenodd"
                  />
                </svg>
              </span>
              <span>Log out</span>
            </div>
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  computed: {
    ...mapGetters(['isAuthenticated', 'authenticatedUser']),
  },
  data() {
    return {
      showMenu: false,
    }
  },
}
</script>

<style></style>
