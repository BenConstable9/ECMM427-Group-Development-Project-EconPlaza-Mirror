<template>
    <main>
        <div class="container mx-auto">
            <div class="bg-gray-100 px-5 mt-5 mb-5 mx-auto">
                <not-found v-if="postNotFound && !loading" id="content" />
                <div v-else id="content" class="flex space-x-5 pt-5 pb-8">
                    <div id="content-left" class="w-full lg:w-3/4">
                        <post-box />
                        <comment-table />
                    </div>
                    <div
                        id="content-left"
                        class="hidden lg:flex lg:w-1/4 flex-col space-y-5"
                    >
                        <post-stat-box />
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
import { PLAZAS } from '~/api-routes'

export default {
    data() {
        return {
            loading: false,
        }
    },
    head() {
        return {
            title: `${this.post.title} | ${this.plaza.name} | EconPlaza`,
        }
    },
    computed: {
        ...mapGetters({
            plaza: 'plazas/currentPlaza',
            post: 'plazas/posts/currentPost',
        }),
        postNotFound() {
            // Determine if post exists if the ID is 0 (the undefined post)
            return this.post && this.post.id === 0
        },
    },
    mounted() {
        this.$axios.post(
            PLAZAS.VIEWPOST(this.$route.params.plazas, this.$route.params.id)
        )
    },
    async created() {
        this.loading = true
        await this.getCurrentPlaza(this.$route.params.plazas)
        await this.getCurrentPost({
            plazaSlug: this.$route.params.plazas,
            postID: this.$route.params.id,
        })
        this.loading = false
    },
    methods: {
        ...mapActions({
            getCurrentPlaza: 'plazas/getCurrentPlaza',
            getCurrentPost: 'plazas/posts/getCurrentPost',
        }),
    },
}
</script>
