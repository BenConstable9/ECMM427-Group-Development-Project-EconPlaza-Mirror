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
                    <Success v-if="success" :message="success" />

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
                                    placeholder="Username"
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
                                    placeholder="Email"
                                />
                            </div>
                        </div>
                        <div class="field">
                            <label class="label">First Name</label>
                            <div class="control">
                                <input
                                    v-model="first_name"
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
                                    name="first_name"
                                    required
                                    placeholder="First Name"
                                />
                            </div>
                        </div>
                        <div class="field">
                            <label class="label">Last Name</label>
                            <div class="control">
                                <input
                                    v-model="last_name"
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
                                    name="last_name"
                                    required
                                    placeholder="Last Name"
                                />
                            </div>
                        </div>
                        <div class="field">
                            <label class="label">Institution</label>
                            <div class="control">
                                <input
                                    v-model="institution"
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
                                    name="institution"
                                    required
                                    placeholder="Institution"
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
                                    placeholder="Password"
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
                        <div class="field">
                            <input
                                id="checkbox"
                                v-model="privacy"
                                type="checkbox"
                            />
                            <label class="label" for="checkbox">
                                I have read and understood the
                                <nuxt-link to="/login">privacy policy</nuxt-link
                                >.
                            </label>
                        </div>
                        <div class="field">
                            <recaptcha />
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
import { USERS } from '../api-routes'
import Error from '~/components/messages/Error'
import Success from '~/components/messages/Success'

export default {
    components: {
        Error,
        Success,
    },

    data() {
        return {
            username: '',
            email: '',
            first_name: '',
            last_name: '',
            insitution: '',
            password: '',
            error: null,
            success: null,
            over18: null,
            privacy: null,
        }
    },
    head() {
        return {
            title: 'Register | EconPlaza',
        }
    },
    auth: 'guest',
    methods: {
        async register() {
            if (this.over18 === true && this.privacy === true) {
                const token = await this.$recaptcha.getResponse()

                // send token to server alongside your form data
                await this.$axios
                    .post(USERS.REGISTER(), {
                        username: this.username,
                        email: this.email,
                        first_name: this.first_name,
                        last_name: this.last_name,
                        institution: this.institution,
                        password: this.password,
                        'g-recaptcha-response': token,
                    })
                    .then(async () => {
                        this.success = 'You are now registered for EconPlaza!'
                        await this.$auth.loginWith('local', {
                            data: {
                                username: this.username,
                                password: this.password,
                            },
                        })
                        this.$router.push('/', {
                            username: this.username,
                            password: this.password,
                        })
                    })
                    .catch((response) => {
                        if (
                            typeof response === 'string' ||
                            response instanceof String
                        ) {
                            this.error = response
                        } else if ('detail' in response) {
                            this.error = response.detail
                        } else {
                            this.error = 'Unable to process request.'
                        }
                    })
                // at the end you need to reset recaptcha
                await this.$recaptcha.reset()
            }
        },
    },
}
</script>
