<template>
    <div>
        <ul
            class="
                w-full
                border
                rounded-r-2xl rounded-b-2xl
                overflow-hidden
                shadow-md
            "
        >
            <voucher-header :first-name="firstName" />
            <Error v-if="error" :message="error" />
            <div class="bg-gray-100 px-4 py-2">
                <form class="space-y-4" @submit.prevent="userVouch">
                    <div>
                        <label
                            >Are you certain that this name belongs to a real
                            person who you know?</label
                        >
                        <input
                            v-model="voucher.name"
                            type="checkbox"
                            :disabled="voucher.isDisabled"
                        />
                    </div>
                    <div>
                        <label
                            >Are you 100% certain that this email belongs to the
                            person named above?</label
                        >
                        <input
                            v-model="voucher.email"
                            type="checkbox"
                            :disabled="voucher.isDisabled"
                        />
                    </div>
                    <div>
                        <label
                            >Are you 100% certain the institutional affiliation
                            and position of the person named above are
                            correct?</label
                        >
                        <input
                            v-model="voucher.institution"
                            type="checkbox"
                            :disabled="voucher.isDisabled"
                        />
                    </div>
                    <div
                        v-if="
                            voucher.name && voucher.email && voucher.institution
                        "
                    >
                        <p>
                            Your vouch will be displayed publicly in this user's
                            profile
                        </p>
                        <button
                            type="submit"
                            :disabled="voucher.isDisabled"
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
import VoucherHeader from '~/components/vouch/voucher-header'

export default {
    name: 'VouchBox',
    components: {
        VoucherHeader,
    },
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
