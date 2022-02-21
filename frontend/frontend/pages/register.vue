<template>
    <div class="w-full max-w-md bg-gray-50 rounded-lg border shadow-sm mx-auto">
        <form
            method="post"
            class="flex flex-col mx-8 mt-8 border-b"
            @submit.prevent="register"
        >
            <h1 class="text-2xl text-gray-800 font-semibold mx-auto mb-3">
                EconPlaza
            </h1>
            <Error v-if="error" :message="error" />
            <Success v-if="success" :message="success" />

            <label class="text-gray-800 mt-5 mb-2" for="username"
                >Username</label
            >

            <input
                v-model="username"
                class="rounded-lg border px-3 py-1.5"
                type="text"
                name="username"
                required
            />

            <label class="text-gray-800 mt-5 mb-2" for="email"
                >Email address</label
            >

            <input
                v-model="email"
                class="rounded-lg border px-3 py-1.5"
                type="email"
                name="email"
                required
            />

            <div id="full-name-container" class="flex space-x-5">
                <div id="first-name-container" class="flex flex-col">
                    <label class="text-gray-800 mt-5 mb-2" for="first_name"
                        >First name</label
                    >

                    <input
                        v-model="first_name"
                        class="w-full rounded-lg border px-3 py-1.5"
                        type="text"
                        name="first_name"
                        required
                    />
                </div>

                <div id="last-name-container" class="flex flex-col">
                    <label class="text-gray-800 mt-5 mb-2" for="last_name"
                        >Last name</label
                    >

                    <input
                        v-model="last_name"
                        class="w-full rounded-lg border px-3 py-1.5"
                        type="text"
                        name="last_name"
                        required
                    />
                </div>
            </div>

            <label
                class="text-gray-800 mt-5 mb-2"
                for="institutional_affiliation"
                >Institution</label
            >

            <input
                v-model="institutional_affiliation"
                class="rounded-lg border px-3 py-1.5"
                type="text"
                name="institutional_affiliation"
                required
            />

            <label class="text-gray-800 mt-5 mb-2" for="password"
                >Password</label
            >

            <input
                v-model="password"
                class="rounded-lg border px-3 py-1.5"
                type="password"
                name="password"
                required
            />

            <label class="text-gray-800 mt-5 mb-3">Verification</label>

            <div class="field h-20">
                <recaptcha />
            </div>

            <label class="text-gray-800 mt-5"></label>

            <div class="field">
                <input id="checkbox" v-model="over18" type="checkbox" />
                <label class="label" for="checkbox">
                    I certify that I am least 18 years of age
                </label>
            </div>
            <div class="field">
                <input id="checkbox" v-model="privacy" type="checkbox" />
                <label class="label" for="checkbox">
                    I have read and understood the
                    <NuxtLink to="#" class="text-blue-600"
                        >privacy policy
                    </NuxtLink>
                </label>
            </div>

            <button
                class="
                    rounded-lg
                    border
                    text-gray-50
                    bg-indigo-500
                    hover:bg-indigo-600
                    duration-100
                    px-3
                    py-2
                    mt-10
                    mb-8
                "
                type="submit"
            >
                Register
            </button>
        </form>
        <div class="flex flex-col mx-5 mt-8 mb-8">
            <h1 class="text-gray-800 mx-auto">
                Already have an account?
                <NuxtLink :to="`/login/`" class="text-blue-700 hover:underline">
                    Log in
                </NuxtLink>
            </h1>
        </div>
    </div>
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
    layout: 'auth',
    data() {
        return {
            username: '',
            email: '',
            first_name: '',
            last_name: '',
            institutional_affiliation: '',
            password: '',
            error: null,
            success: null,
            over18: null,
            privacy: null,
        }
    },
    head() {
        return {
            title: 'Register',
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
                        institutional_affiliation:
                            this.institutional_affiliation,
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
                    .catch((err) => {
                        // If there is an error set the error message to
                        // '' instead of null for display purposes
                        this.error = ''
                        if (typeof err === 'string' || err instanceof String) {
                            this.error = err
                        } else if ('detail' in err.response) {
                            Object.values(err.response.detail).forEach(
                                (val) => {
                                    this.error += val + ' '
                                }
                            )
                        } else if ('data' in err.response) {
                            Object.values(err.response.data).forEach((val) => {
                                this.error += val + ' '
                            })
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
