<template>
    <div class="flex items-center px-5 py-3 bg-primary">
        <h3
            class="
                flex-1
                text-gray-50
                hover:underline
                duration-100
                text-xl
                font-semibold
            "
        >
            <NuxtLink :to="`/plazas/${slug}`">
                {{ name }}
            </NuxtLink>
        </h3>
        <template v-if="isMember">
            <div class="rounded-full bg-gray-100 p-3">
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-5 w-5 text-primary mx-auto"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                >
                    <path
                        fill-rule="evenodd"
                        d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                        clip-rule="evenodd"
                    />
                </svg>
            </div>
        </template>
        <template v-else>
            <button
                class="
                    rounded-full
                    text-gray-400
                    hover:text-secondary
                    bg-gray-100
                    duration-100
                    p-3
                "
                @click="plazaJoin()"
            >
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-5 w-5 mx-auto"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                >
                    <path
                        fill-rule="evenodd"
                        d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-11a1 1 0 10-2 0v2H7a1 1 0 100 2h2v2a1 1 0 102 0v-2h2a1 1 0 100-2h-2V7z"
                        clip-rule="evenodd"
                    />
                </svg>
            </button>
        </template>
    </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
    name: 'PlazaBoxHeader',
    props: {
        slug: { type: String, default: '' },
        name: { type: String, default: '' },
        isMember: { type: Boolean, default: false },
    },
    methods: {
        ...mapActions({
            joinPlaza: 'plazas/joinPlaza',
        }),
        plazaJoin() {
            // Join the plaza
            this.joinPlaza({ plazaSlug: this.slug })
        },
    },
}
</script>

<style></style>
