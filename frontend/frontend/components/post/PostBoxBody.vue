<template>
    <div>
        <div class="bg-gray-50 px-5 py-3">
            <MarkdownViewer :content="post.content" />
        </div>
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import MarkdownViewer from '~/components/post/MarkdownViewer'

export default {
    components: { MarkdownViewer },
    computed: {
        ...mapGetters({
            post: 'plazas/posts/currentPost',
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
