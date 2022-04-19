<template>
    <div>
        <Error v-if="error" :message="error" />
        <Success v-if="success" :message="success" />
        <div id="post-heading" class="bg-primary px-5 py-3">
            <div class="flex space-x-3 items-center">
                <div v-if="includePlazaActions" id="title" class="flex-1">
                    <div class="flex flex-col space-y-1">
                        <h1 class="text-gray-50 text-xl font-semibold">
                            {{ loading ? '' : plaza.name }}
                        </h1>
                        <h2 class="italic text-gray-100">
                            {{ loading ? '' : plaza.description }}
                        </h2>
                    </div>
                </div>
                <div v-else id="title" class="flex-1">
                    <div class="flex flex-col space-y-1">
                        <h1 class="text-gray-50 text-xl font-semibold">
                            {{ title }}
                        </h1>
                        <h2 class="italic text-gray-100">{{ description }}</h2>
                    </div>
                </div>
                <pagination-size :size="pagination.preferredSize" />
                <pagination-sort
                    :sort="pagination.desiredSort"
                    :options="pagination.sortOptions"
                />
                <div
                    v-if="
                        authenticatedUser.verified &&
                        plaza.membership.member &&
                        includePlazaActions
                    "
                    id="write"
                >
                    <NuxtLink :to="`/plazas/${plaza.slug}/create`">
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
                <div v-if="includePlazaActions" id="join">
                    <template v-if="plaza.membership.member">
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
                                hover:text-primary
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
                <!-- For Future Dropdown <div id="views">
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
                </div> -->
            </div>
            <div v-if="includePlazaActions" class="flex flex-wrap mt-2">
                <Tag
                    v-for="tagged in plaza.tags"
                    :key="tagged.id"
                    :slug="tagged.tag.name"
                />
            </div>
        </div>
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import Error from '~/components/messages/Error'
import Success from '~/components/messages/Success'
import Tag from '~/components/labels/Tag'
import PaginationSize from '~/components/helpers/PaginationSize'
import PaginationSort from '~/components/helpers/PaginationSort'

export default {
    components: {
        Error,
        Success,
        Tag,
        PaginationSize,
        PaginationSort,
    },
    props: {
        includePlazaActions: { type: Boolean, default: true },
        title: { type: String, default: '' },
        description: { type: String, default: '' },
    },
    data() {
        return {
            loading: false,
            error: null,
            success: null,
            membership: {
                isDisabled: null,
            },
        }
    },
    computed: {
        ...mapGetters({
            plaza: 'plazas/currentPlaza',
            authenticatedUser: 'authenticatedUser',
            pagination: 'plazas/posts/pagination',
        }),
    },
    async created() {
        this.loading = true
        if (this.includePlazaActions) {
            await this.getCurrentPlaza({ plazaSlug: this.$route.params.plazas })
        }
        this.loading = false
    },
    methods: {
        ...mapActions({
            getCurrentPlaza: 'plazas/getCurrentPlaza',
            joinPlaza: 'plazas/joinPlaza',
        }),
        plazaJoin() {
            this.membership.isDisabled = true

            this.joinPlaza({ plazaSlug: this.$route.params.plazas })
        },
    },
}
</script>
