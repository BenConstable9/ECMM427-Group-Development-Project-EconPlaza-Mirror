<template>
    <div class="flex items-center space-x-4">
        <div id="profile">
            <div
                class="flex items-center space-x-2 cursor-pointer"
                @click="showVouchModal = !showVouchModal"
            >
                <div
                    class="
                        font-semibold
                        bg-gray-50
                        hover:bg-gray-200
                        rounded
                        pl-2.5
                        pr-1.5
                        py-0.5
                        border
                        transition
                    "
                >
                    <div class="flex space-x-2">
                        <span class="text-sm text-gray-700 mx-auto">Vouch</span
                        ><svg
                            xmlns="http://www.w3.org/2000/svg"
                            class="h-5 w-5 text-gray-700"
                            viewBox="0 0 20 20"
                            fill="currentColor"
                        >
                            <path
                                d="M8 9a3 3 0 100-6 3 3 0 000 6zM8 11a6 6 0 016 6H2a6 6 0 016-6zM16 7a1 1 0 10-2 0v1h-1a1 1 0 100 2h1v1a1 1 0 102 0v-1h1a1 1 0 100-2h-1V7z"
                            />
                        </svg>
                    </div>
                </div>
            </div>
            <VouchModal
                :id="id"
                v-model="showVouchModal"
                :first-name="firstName"
                :last-name="lastName"
                :email="email"
                :affiliation="affiliation"
            />
        </div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
import VouchModal from './VouchModal'
export default {
    components: { VouchModal },
    props: {
        id: { type: Number, default: null },
        firstName: { type: String, default: null },
        lastName: { type: String, default: null },
        email: { type: String, default: null },
        affiliation: { type: String, default: null },
    },
    data() {
        return {
            showVouchModal: false,
        }
    },
    computed: {
        ...mapGetters(['isAuthenticated', 'authenticatedUser']),
    },
    mounted() {
        this.$nuxt.$on('user-vouched', () => {
            this.showVouchModal = false
        })
    },
}
</script>

<style></style>
