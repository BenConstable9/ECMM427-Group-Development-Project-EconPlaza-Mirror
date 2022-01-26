<template>
    <div id="about-info" class="flex bg-gray-50 px-5 py-3">
        <div class="flex-1 text-gray-900">
            <p class="text-sm">Members</p>
            <p>{{ members }}</p>
        </div>
        <div class="flex-1 text-gray-900">
            <p class="text-sm">Posts</p>
            <p>{{ posts }}</p>
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
        ...mapGetters({ plaza: 'plazas/currentPlaza' }),
        members() {
            return this.plaza ? this.plaza.stats.members : ''
        },
        posts() {
            return this.plaza ? this.plaza.stats.posts : ''
        },
    },
    async created() {
        this.loading = true
        await this.getCurrentPlaza({ plazaSlug: this.$route.params.plazas })
        this.loading = false
    },
    methods: {
        ...mapActions({
            getCurrentPlaza: 'plazas/getCurrentPlaza',
        }),
    },
}
</script>

<style></style>
