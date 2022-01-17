<template>
    <main>
        <div class="container mx-auto">
            <div class="bg-gray-100 px-5 mt-5 mb-5 mx-auto">
                <div
                    v-if="plazaNotFound && !loading"
                    id="content"
                    class="flex space-x-5 pt-5 pb-8"
                >
                    <div id="content-left" class="w-full lg:w-3/4">
                        <h1 class="text-primary text-2xl my-10">
                            Plaza Not Found!
                        </h1>
                        <p class="text-gray-500">
                            We can't seem to find this plaza, it may have been
                            removed or deleted
                        </p>
                        <p class="my-5">
                            <NuxtLink
                                to="/"
                                class="
                                    px-5
                                    py-2
                                    rounded-lg
                                    bg-primary
                                    text-gray-100
                                    hover:bg-secondary
                                "
                            >
                                Take Me Home
                            </NuxtLink>
                        </p>
                    </div>
                    <div
                        id="content-left"
                        class="hidden lg:flex lg:w-1/4 flex-col space-y-5"
                    >
                        <my-plazas />
                        <my-bookmarks />
                        <popular-plazas />
                    </div>
                </div>
                <div v-else id="content" class="flex space-x-5 pt-5 pb-8">
                    <div id="content-left" class="w-full lg:w-3/4">
                        <post-table />
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
            title: `${this.plaza.name} | EconPlaza`,
        }
    },
    computed: {
        ...mapGetters({ plaza: 'plazas/current', posts: 'plazas/posts/posts' }),
        plazaNotFound() {
            // Determine if plaza exists if the ID is 0 (the undefined plaza)
            return this.plaza && this.plaza.id === 0
        },
    },
    async created() {
        this.loading = true
        await this.getCurrentPlaza(this.$route.params.plazas)
        await this.getAllPlazaPosts(this.$route.params.plazas)
        this.loading = false
    },
    methods: {
        ...mapActions({
            getCurrentPlaza: 'plazas/getCurrentPlaza',
            getAllPlazaPosts: 'plazas/posts/getAllPlazaPosts',
        }),
    },
}
</script>
