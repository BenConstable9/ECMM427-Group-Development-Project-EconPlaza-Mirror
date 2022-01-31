<template>
    <div
        id="about-heading"
        class="flex space-x-3 items-center bg-primary px-5 py-3"
    >
        <div id="title" class="flex-1">
            <div class="flex flex-col space-y-1">
                <h1 class="text-gray-50 text-lg font-semibold">
                    About {{ plaza.name }}
                </h1>
            </div>
        </div>
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
