<template>
    <div>
        <ul>
            <div
                id="memberships-heading"
                class="flex space-x-3 items-center bg-primary px-5 py-3"
            >
                <div id="title" class="flex-1">
                    <div class="flex flex-col space-y-1">
                        <h1 class="text-gray-50 text-lg font-semibold">
                            Vouch for {{ firstName }}?
                        </h1>
                    </div>
                </div>
            </div>
            <Error v-if="error" :message="error" />
            <div class="bg-gray-50 px-5 py-5">
                <form class="space-y-4" @submit.prevent="userVouch">
                    <p>Please check the following:</p>
                    <div class="flex items-center space-x-5">
                        <input
                            v-model="voucher.name"
                            type="checkbox"
                            :disabled="voucher.isDisabled"
                        />
                        <label
                            >Are you certain that this name belongs to a real
                            person who you know?</label
                        >
                    </div>
                    <div class="flex items-center space-x-5">
                        <input
                            v-model="voucher.email"
                            type="checkbox"
                            :disabled="voucher.isDisabled"
                        />
                        <label
                            >Are you 100% certain that this email belongs to the
                            person named above?</label
                        >
                    </div>
                    <div class="flex items-center space-x-5">
                        <input
                            v-model="voucher.institution"
                            type="checkbox"
                            :disabled="voucher.isDisabled"
                        />
                        <label
                            >Are you 100% certain the institutional affiliation
                            and position of the person named above are
                            correct?</label
                        >
                    </div>
                    <div>
                        <p
                            class="
                                mt-5
                                disabled:invisible
                                transition
                                text-gray-700
                            "
                            :class="{
                                'opacity-0':
                                    !voucher.name ||
                                    !voucher.email ||
                                    !voucher.institution,
                                'opacity-100':
                                    voucher.name &&
                                    voucher.email &&
                                    voucher.institution,
                            }"
                        >
                            Your vouch will be displayed publicly in this user's
                            profile.
                        </p>
                        <button
                            type="submit"
                            :disabled="
                                !voucher.name ||
                                !voucher.email ||
                                !voucher.institution
                            "
                            class="
                                text-gray-100
                                font-semibold
                                rounded
                                py-1
                                px-5
                                mt-3
                                transition
                                duration-200
                            "
                            :class="{
                                'bg-primary hover:bg-blue-600 text-gray-50':
                                    voucher.name &&
                                    voucher.email &&
                                    voucher.institution,
                                'bg-gray-100 text-gray-300 ring-1 ring-gray-300':
                                    !voucher.name ||
                                    !voucher.email ||
                                    !voucher.institution,
                            }"
                        >
                            Vouch
                        </button>
                    </div>
                </form>
            </div>
        </ul>
    </div>
</template>

<script>
import { USERS } from '../../api-routes'

export default {
    name: 'VouchBox',
    props: {
        id: { type: Number, default: null },
        firstName: { type: String, default: null },
        vouches: { type: Array, default: null },
    },
    data() {
        return {
            voucher: {
                name: false,
                email: false,
                institution: false,
                isDisabled: false,
            },
            error: null,
        }
    },
    methods: {
        async userVouch() {
            this.voucher.isDisabled = true

            // Send to server
            await this.$axios
                .post(USERS.VOUCHES(this.id), {
                    vouchee: this.id,
                    voucher: this.$store.getters.authenticatedUser.id,
                })
                .then(this.$nuxt.$emit('user-vouched'))
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

                    this.voucher.isDisabled = false
                })
        },
    },
}
</script>

<style></style>
