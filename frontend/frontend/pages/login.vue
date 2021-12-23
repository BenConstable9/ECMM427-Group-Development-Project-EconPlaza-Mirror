<template>
  <main>
    <div class="container mx-auto flex justify-center items-center">
      <div
        class="
          max-w-md
          w-full
          bg-gray-200
          rounded-r-2xl rounded-b-2xl
          p-4
          m-10
          space-y-4
        "
      >
        <div class="mb-4">
          <h2 class="text-xl font-bold">Login to EconPlaza</h2>
        </div>
        <Notification v-if="error" :message="error" />
        <form class="space-y-4" @submit.prevent="userLogin">
          <div>
            <input
              v-model="login.username"
              class="
                w-full
                p-4
                text-m
                bg-white
                focus:outline-none
                border border-gray-200
                rounded-r-2xl rounded-b-2xl
                text-blue-600
              "
              type="text"
              placeholder="Username"
            />
          </div>
          <div>
            <input
              v-model="login.password"
              class="
                w-full
                p-4
                text-m
                bg-white
                focus:outline-none
                border border-gray-200
                rounded-r-2xl rounded-b-2xl
                text-blue-600
              "
              type="password"
              placeholder="Password"
            />
          </div>
          <div>
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
                text-white
                transition
                duration-200
              "
            >
              Login
            </button>
          </div>
        </form>
      </div>
    </div>
  </main>
</template>

<script>
import Notification from '~/components/helpers/Notification'

export default {
  components: {
    Notification,
  },
  data() {
    return {
      login: {
        username: '',
        password: '',
      },
      error: null,
    }
  },
  head() {
    return {
      title: 'Login | EconPlaza',
    }
  },
  auth: 'guest',
  methods: {
    async userLogin() {
      try {
        await this.$auth.loginWith('local', { data: this.login })

        this.$router.push('/')
      } catch (err) {
        if ('detail' in err.response.data) {
          this.error = err.response.data.detail
        } else if (
          'username' in err.response.data ||
          'password' in err.response.data
        ) {
          this.error = 'Username and password field cannot be blank.'
        } else {
          this.error = 'Unable to process request.'
        }
      }
    },
  },
}
</script>
