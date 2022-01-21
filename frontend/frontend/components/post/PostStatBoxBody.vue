<template>
    <div id="about-info" class="flex bg-gray-50 px-5 py-3">
        <div class="flex-1 text-gray-900">
            <p class="text-sm">Views</p>
            <p>{{ views }}</p>
        </div>
        <div class="flex-1 text-gray-900">
            <p class="text-sm">Replies</p>
            <p>{{ replies }}</p>
        </div>
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
    data() {
        return {
            loading: false,
        }
    },
    computed: {
        ...mapGetters({ post: 'plazas/posts/current' }),
        views() {
            return this.post ? this.post.views : ''
        },
        replies() {
            return this.post ? this.post.replies : ''
        },
    },
    async created() {
        this.loading = true
        await this.getCurrentPost({
            plazaSlug: this.$route.params.plazas,
            postID: this.$route.params.id,
        })
        this.loading = false
    },
    methods: {
        ...mapActions({
            getCurrentPost: 'plazas/getCurrentPost',
        }),
    },
}
</script>

<style></style>
