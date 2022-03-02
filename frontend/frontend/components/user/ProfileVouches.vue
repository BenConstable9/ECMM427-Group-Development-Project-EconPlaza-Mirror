<template>
    <div id="vouches" class="bg-gray-50 rounded-lg border overflow-hidden">
        <div id="vouches-details" class="flex flex-col justify-center">
            <div
                id="vouches-heading"
                class="flex space-x-3 items-center bg-primary px-5 py-3"
            >
                <div id="title" class="flex-1">
                    <div class="flex justify-between">
                        <h1 class="text-gray-50 text-lg font-semibold">
                            Vouches
                        </h1>
                        <span v-if="canVouch">
                            <VouchModalToggle
                                :id="user.id"
                                v-model="showVouchModal"
                                :first-name="user.first_name"
                            />
                        </span>
                    </div>
                </div>
            </div>
            <div class="flex-col divide-y px-5 py-2">
                <template v-if="vouches.length == 0">
                    <div class="italic text-gray-600 py-1">
                        User has no vouches.
                    </div>
                </template>
                <template v-else>
                    <ProfileVouch
                        v-for="vouch in vouches"
                        :key="vouch.id"
                        :vouch="vouch"
                    />
                </template>
            </div>
        </div>
    </div>
</template>

<script>
import VouchModalToggle from '~/components/user/VouchModalToggle'

export default {
    components: {
        VouchModalToggle,
    },
    props: {
        user: {
            type: Object,
            default: () => {},
        },
        vouches: {
            type: Array,
            default: () => [],
        },
        canVouch: { type: Boolean, default: false },
    },
    data() {
        return {
            showVouchModal: true,
        }
    },
}
</script>
