<template>
    <div class="w-full max-w-md bg-gray-50 rounded-lg border shadow-sm mx-auto">
        <form
            class="flex flex-col mx-8 mt-8 border-b"
            @submit.prevent="userLogin"
        >
            <h1 class="text-2xl text-gray-800 font-semibold mx-auto">
                EconPlaza
            </h1>
            <Error v-if="error" :message="error" />

            <label class="text-gray-800 mt-8 mb-3" for="username"
                >Username</label
            >

            <input
                v-model="login.username"
                :disabled="login.isDisabled"
                class="
                    rounded-lg
                    border
                    px-3
                    py-2
                    disabled:bg-gray-100 disabled:text-gray-500
                "
                type="text"
                name="username"
            />

            <label class="text-gray-800 mt-5 mb-3" for="password"
                >Password</label
            >

            <input
                v-model="login.password"
                :disabled="login.isDisabled"
                class="
                    rounded-lg
                    border
                    px-3
                    py-2
                    disabled:bg-gray-100 disabled:text-gray-500
                "
                type="password"
                name="password"
            />

            <label class="text-gray-800 mt-5 mb-3">Verification</label>

            <div class="field">
                <recaptcha />
            </div>

            <button
                :disabled="login.isDisabled"
                class="
                    rounded-lg
                    border
                    text-gray-50
                    bg-primary
                    hover:bg-blue-500
                    duration-100
                    px-3
                    py-2
                    mt-10
                    mb-8
                    disabled:bg-gray-100
                    disabled:text-gray-500
                    disabled:border-gray-400
                "
                type="submit"
            >
                Log in
            </button>
        </form>
        <div class="flex flex-col mx-5 mt-8 mb-8">
            <h1 class="text-gray-800 mx-auto">
                Need an account?
                <NuxtLink
                    :to="`/register/`"
                    class="text-blue-700 hover:underline"
                >
                    Sign up
                </NuxtLink>
            </h1>
        </div>
    </div>
</template>

<script>
import Error from '~/components/messages/Error'

export default {
    components: {
        Error,
    },
    layout: 'auth',
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
        register() {
            this.$router.push('/register')
        },
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
