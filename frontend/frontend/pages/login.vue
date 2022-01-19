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
                    shadow-md
                "
            >
                <div class="mb-4">
                    <h2 class="text-xl font-bold">Login to EconPlaza</h2>
                </div>
                <Error v-if="error" :message="error" />
                <form class="space-y-4" @submit.prevent="userLogin">
                    <div>
                        <input
                            v-model="login.username"
                            :disabled="login.isDisabled"
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
                            type="text"
                            placeholder="Username"
                        />
                    </div>
                    <div>
                        <input
                            v-model="login.password"
                            :disabled="login.isDisabled"
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
                            type="password"
                            placeholder="Password"
                        />
                    </div>
                    <div>
                        <button
                            type="submit"
                            :disabled="login.isDisabled"
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
                            Login
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </main>
</template>

<script>
import Error from '~/components/helpers/error'

export default {
    components: {
        Error,
    },
    data() {
        return {
            login: {
                username: '',
                password: '',
                isDisabled: false,
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
                this.login.isDisabled = true
                await this.$auth.loginWith('local', { data: this.login })

                this.$router.push('/')
            } catch (err) {
                // This handles cases where the API is offline so no detailed response is sent back
                if (
                    typeof err.response.data === 'string' ||
                    err.response.data instanceof String
                ) {
                    this.error = err.response.data
                } else if ('detail' in err.response.data) {
                    this.error = err.response.data.detail
                } else if (
                    'username' in err.response.data ||
                    'password' in err.response.data
                ) {
                    this.error = 'Username and password field cannot be blank.'
                } else {
                    this.error = 'Unable to process request.'
                }
            } finally {
                this.login.isDisabled = false
            }
        },
    },
}
</script>
