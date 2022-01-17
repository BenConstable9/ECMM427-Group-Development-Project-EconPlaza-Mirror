<template>
    <div
        id="post-heading"
        class="flex space-x-3 items-center bg-primary px-5 py-3"
    >
        <div id="title" class="flex-1">
            <div class="flex flex-col space-y-1">
                <h1 class="text-gray-50 text-xl font-semibold">
                    {{ loading ? '' : plaza.name }}
                </h1>
                <h2 class="italic text-gray-100">
                    {{ loading ? '' : plaza.description }}
                </h2>
            </div>
        </div>
        <div v-if="authenticatedUser.verified" id="write">
            <NuxtLink :to="`${plaza.slug}/posts`">
                <div class="rounded-full bg-gray-50 p-3">
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        class="h-5 w-5 text-primary mx-auto"
                        viewBox="0 0 20 20"
                        fill="currentColor"
                    >
                        <path
                            d="M17.414 2.586a2 2 0 00-2.828 0L7 10.172V13h2.828l7.586-7.586a2 2 0 000-2.828z"
                        />
                        <path
                            fill-rule="evenodd"
                            d="M2 6a2 2 0 012-2h4a1 1 0 010 2H4v10h10v-4a1 1 0 112 0v4a2 2 0 01-2 2H4a2 2 0 01-2-2V6z"
                            clip-rule="evenodd"
                        />
                    </svg>
                </div>
            </NuxtLink>
        </div>
        <div id="views">
            <div class="rounded-full bg-gray-50 p-3">
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-5 w-5 text-primary mx-auto"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                >
                    <path
                        d="M6 10a2 2 0 11-4 0 2 2 0 014 0zM12 10a2 2 0 11-4 0 2 2 0 014 0zM16 12a2 2 0 100-4 2 2 0 000 4z"
                    />
                </svg>
            </div>
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
        ...mapGetters({
            plaza: 'plazas/current',
            authenticatedUser: 'authenticatedUser',
        }),
    },
    async created() {
        this.loading = true
        await this.getCurrentPlaza(this.$route.params.plazas)
        this.loading = false
    },
    methods: {
        ...mapActions({
            getCurrentPlaza: 'plazas/getCurrentPlaza',
        }),
    },
}
</script>
