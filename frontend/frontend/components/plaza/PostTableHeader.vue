<template>
    <div>
        <Error v-if="error" :message="error" />
        <Success v-if="success" :message="success" />
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
            <pagination-size :size="pagination.preferredSize" />
            <div v-if="plaza.membership.member" id="write">
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
            <div v-else id="join">
                <form @submit.prevent="plazaJoin">
                    <button
                        class="rounded-full bg-gray-50 p-3"
                        type="submit"
                        :disabled="membership.isDisabled"
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
                </form>
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
    </div>
</template>

<script>
import { mapGetters, mapActions, mapMutations } from 'vuex'
import Error from '~/components/messages/Error'
import Success from '~/components/messages/Success'
import PaginationSize from '~/components/helpers/PaginationSize'
import { PLAZAS } from '~/api-routes'

export default {
    components: {
        Error,
        Success,
        PaginationSize,
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
        await this.getCurrentPlaza({ plazaSlug: this.$route.params.plazas })
        this.loading = false
    },
    methods: {
        ...mapActions({
            getCurrentPlaza: 'plazas/getCurrentPlaza',
        }),
        ...mapMutations({
            joinCurrentPlaza: 'plazas/joinCurrentPlaza',
        }),
        async plazaJoin() {
            this.membership.isDisabled = true

            const memberType = 'MB'

            // Send to server
            await this.$axios
                .post(PLAZAS.MEMBERSHIP(this.$route.params.plazas), {
                    user: this.$store.getters.authenticatedUser.id,
                    plaza: this.$route.params.plazas,
                    member_type: memberType,
                })
                .then(() => {
                    this.joinCurrentPlaza(memberType)
                    this.success = 'Joined Plaza!'
                })
                .catch((response) => {
                    if (
                        typeof response === 'string' ||
                        response instanceof String
                    ) {
                        this.error = response
                    } else if ('detail' in response) {
                        this.error = response.detail
                    } else {
                        this.error = 'Unable to process request.'
                    }

                    this.membership.isDisabled = false
                })
        },
    },
}
</script>
