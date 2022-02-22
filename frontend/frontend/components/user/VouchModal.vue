<template>
    <div class="relative">
        <div
            class="
                fixed
                top-0
                right-0
                z-10
                h-screen
                w-screen
                bg-black
                transition
            "
            :class="{
                'invisible opacity-0': !value,
                'visible opacity-20': value,
            }"
            @click="toggleMenu"
        ></div>
        <div
            id="dropdown"
            class="
                fixed
                w-full
                max-w-lg
                items-center
                rounded-lg
                shadow-lg
                overflow-hidden
                z-20
                top-1/2
                left-1/2
                transition
                transform
                -translate-x-1/2 -translate-y-1/2
            "
            :class="{
                'pointer-events-none opacity-0 scale-95': !value,
                'pointer-events-auto opacity-100 scale-100': value,
            }"
        >
            <Voucher :id="id" :first-name="firstName" />
        </div>
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import Voucher from '~/components/user/Voucher'

export default {
    name: 'Dropdown',
    components: {
        Voucher,
    },
    props: {
        id: { type: Number, default: null },
        firstName: { type: String, default: null },
        value: {
            type: Boolean,
            default: false,
        },
    },
    computed: {
        ...mapGetters({
            authenticatedUser: 'authenticatedUser',
        }),
    },
    methods: {
        toggleMenu() {
            this.$emit('input', !this.value)
        },
        ...mapActions({ getAllPlazas: 'plazas/getAllPlazas' }),
    },
}
</script>

<style scoped></style>
