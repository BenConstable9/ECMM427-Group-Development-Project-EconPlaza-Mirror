<template>
    <div id="about" class="flex">
        <ul class="flex flex-col w-full border rounded-lg overflow-hidden">
            <about-box-header />
            <about-box-stats />
            <about-box-guest v-if="!plaza.membership.member" />
        </ul>
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
    computed: {
        ...mapGetters({ plaza: 'plazas/currentPlaza' }),
    },
    async created() {
        await this.getCurrentPlaza({ plazaSlug: this.$route.params.plazas })
    },
    methods: {
        ...mapActions({
            getCurrentPlaza: 'plazas/getCurrentPlaza',
        }),
    },
}
</script>

<style></style>
