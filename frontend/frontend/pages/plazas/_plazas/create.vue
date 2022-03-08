<template>
    <main>
        <div class="container mx-auto">
            <div class="bg-gray-100 px-5 mb-5 mx-auto">
                <not-found v-if="plazaNotFound && !loading" id="content" />
                <div v-else id="content" class="flex space-x-5 pt-5 pb-8">
                    <div id="content-left" class="w-full lg:w-3/4">
                        <post-form />
                    </div>
                    <div
                        id="content-left"
                        class="hidden lg:flex lg:w-1/4 flex-col space-y-5"
                    >
                        <about-box />
                        <rules-box />
                    </div>
                </div>
            </div>
        </div>
    </main>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
    data() {
        return {
            loading: false,
        }
    },
    head() {
        return {
            title: `New Post | ${this.plaza.name}`,
        }
    },
    computed: {
        ...mapGetters({ plaza: 'plazas/currentPlaza' }),
        plazaNotFound() {
            // Determine if plaza exists if the ID is 0 (the undefined plaza)
            return this.plaza && this.plaza.id === 0
        },
    },
    async created() {
        this.loading = true
        await this.getCurrentPlaza({ plazaSlug: this.$route.params.plazas })
        this.loading = false
    },
    methods: {
        ...mapActions({ getCurrentPlaza: 'plazas/getCurrentPlaza' }),
    },
}
</script>
