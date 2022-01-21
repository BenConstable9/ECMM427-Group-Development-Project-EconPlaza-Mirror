<template>
    <div>
        <div class="bg-gray-50 px-5 py-3">
            {{ post.content }}
        </div>
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
export default {
    computed: {
        ...mapGetters({
            post: 'plazas/posts/current',
        }),
    },
    async created() {
        await this.getCurrentPost({
            plazaSlug: this.$route.params.plazas,
            postID: this.$route.params.id,
        })
    },
    methods: {
        ...mapActions({
            getCurrentPost: 'plazas/posts/getCurrentPost',
        }),
    },
}
</script>
