<template>
    <div class="flex items-start bg-blue-600 px-4 py-2">
        <h3
            class="
                flex-1
                md:flex-none
                lg:flex-1
                text-lg
                font-semibold
                text-white
            "
        >
            <NuxtLink :to="`/plazas/${slug}`">
                {{ name }}
            </NuxtLink>
        </h3>
        <member
            v-if="isMember"
            class="flex-initial md:flex-none lg:flex-initial"
        />
        <button
            v-else
            class="rounded-full bg-gray-50 p-3"
            @click="$nuxt.$emit('join-plaza', slug)"
        >
            <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5 text-primary mx-auto"
                viewBox="0 0 20 20"
                fill="currentColor"
            >
                <path
                    d="M8 9a3 3 0 100-6 3 3 0 000 6zM8 11a6 6 0 016 6H2a6 6 0 016-6zM16 7a1 1 0 10-2 0v1h-1a1 1 0 100 2h1v1a1 1 0 102 0v-1h1a1 1 0 100-2h-1V7z"
                />
            </svg>
        </button>
    </div>
</template>

<script>
import Member from '~/components/labels/member'

export default {
    name: 'PlazaBoxHeader',
    components: {
        Member,
    },
    props: {
        slug: { type: String, default: '' },
        name: { type: String, default: '' },
        isMember: { type: Boolean, default: false },
    },
}
</script>

<style></style>
