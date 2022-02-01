<template>
    <section class="section">
        <div class="container mx-auto flex justify-center items-center">
            <div
                class="
                    columns
                    max-w-md
                    w-full
                    bg-gray-200
                    rounded-r-2xl rounded-b-2xl
                    p-4
                    m-10
                    space-y-4
                    shadow-md
                "
            >
                <div class="column is-4 is-offset-4">
                    <div class="mb-4">
                        <h2 class="text-xl font-bold">
                            Register for EconPlaza
                        </h2>
                    </div>
                    <Error v-if="error" :message="error" />

                    <form
                        method="post"
                        class="space-y-4"
                        @submit.prevent="register"
                    >
                        <div class="field">
                            <label class="label">Username</label>
                            <div class="control">
                                <input
                                    v-model="username"
                                    type="text"
                                    class="
                                        w-full
                                        p-4
                                        text-m
                                        bg-white
                                        focus:outline-none
                                        border border-gray-200
                                        rounded-r-2xl rounded-b-2xl
                                        text-blue-600
                                        shadow
                                        disabled:bg-gray-100
                                        disabled:text-gray-500
                                        disabled:border-gray-400
                                    "
                                    name="username"
                                    required
                                />
                            </div>
                        </div>
                        <div class="field">
                            <label class="label">Email</label>
                            <div class="control">
                                <input
                                    v-model="email"
                                    type="email"
                                    class="
                                        w-full
                                        p-4
                                        text-m
                                        bg-white
                                        focus:outline-none
                                        border border-gray-200
                                        rounded-r-2xl rounded-b-2xl
                                        text-blue-600
                                        shadow
                                        disabled:bg-gray-100
                                        disabled:text-gray-500
                                        disabled:border-gray-400
                                    "
                                    name="email"
                                    required
                                />
                            </div>
                        </div>
                        <div class="field">
                            <label class="label">Password</label>
                            <div class="control">
                                <input
                                    v-model="password"
                                    type="password"
                                    class="
                                        w-full
                                        p-4
                                        text-m
                                        bg-white
                                        focus:outline-none
                                        border border-gray-200
                                        rounded-r-2xl rounded-b-2xl
                                        text-blue-600
                                        shadow
                                        disabled:bg-gray-100
                                        disabled:text-gray-500
                                        disabled:border-gray-400
                                    "
                                    name="password"
                                    required
                                />
                            </div>
                        </div>
                        <div class="field">
                            <input
                                id="checkbox"
                                v-model="over18"
                                type="checkbox"
                            />
                            <label class="label" for="checkbox">
                                I certify that I am least 18 years of age.
                            </label>
                        </div>
                        <div class="control">
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
                                Register
                            </button>
                        </div>
                    </form>

                    <div class="has-text-centered" style="margin-top: 20px">
                        Already got an account?
                        <nuxt-link to="/login">Login</nuxt-link>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import Error from '~/components/helpers/Error'

export default {
    components: {
        Error,
    },

    data() {
        return {
            username: '',
            email: '',
            password: '',
            error: null,
            over18: null,
        }
    },
    auth: 'guest',
    methods: {
        register() {
            if (this.over18 === true) {
                try {
                    this.$axios.post('v1/accounts/register', {
                        username: this.username,
                        email: this.email,
                        password: this.password,
                    })

                    this.$router.push('/')
                } catch (e) {
                    this.error = e.response.data.message
                }
            }
        },
    },
}
</script>
