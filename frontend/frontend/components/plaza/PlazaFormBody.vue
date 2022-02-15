<template>
    <div>
        <ul class="w-full overflow-hidden">
            <Error v-if="error" :message="error" />
            <div
                id="plaza-heading"
                class="flex space-x-3 items-center px-5 py-3"
            >
                <form class="space-y-4 w-full" @submit.prevent="plazaNew">
                    <div>
                        <input
                            v-model="plaza.name"
                            :disabled="plaza.isDisabled"
                            class="
                                w-full
                                p-4
                                text-m
                                bg-white
                                focus:outline-none
                                border border-gray-200
                                rounded-lg
                                text-primary
                                disabled:bg-gray-100
                                disabled:text-gray-500
                                disabled:border-gray-400
                            "
                            type="text"
                            placeholder="Plaza Name"
                            maxlength="32"
                        />
                    </div>
                    <div>
                        <input
                            v-model="plaza.slug"
                            :disabled="plaza.isDisabled"
                            class="
                                w-full
                                p-4
                                text-m
                                bg-white
                                focus:outline-none
                                border border-gray-200
                                rounded-lg
                                text-primary
                                disabled:bg-gray-100
                                disabled:text-gray-500
                                disabled:border-gray-400
                            "
                            type="text"
                            placeholder="Plaza Slug"
                            maxlength="32"
                        />
                    </div>
                    <div>
                        <textarea
                            v-model="plaza.description"
                            :disabled="plaza.isDisabled"
                            class="
                                w-full
                                p-4
                                text-m
                                bg-white
                                focus:outline-none
                                border border-gray-200
                                rounded-lg
                                text-primary
                                disabled:bg-gray-100
                                disabled:text-gray-500
                                disabled:border-gray-400
                            "
                            type="text"
                            placeholder="Plaza Description"
                            maxlength="2800"
                        >
                        </textarea>
                    </div>
                    <div
                        v-if="
                            plaza.name.length > 0 &&
                            plaza.name.length <= 32 &&
                            plaza.description.length > 0 &&
                            plaza.description.length <= 2800
                        "
                    >
                        <button
                            type="submit"
                            :disabled="plaza.isDisabled"
                            class="
                                w-full
                                py-4
                                bg-primary
                                hover:bg-secondary
                                rounded-lg
                                text-m
                                font-bold
                                text-white
                                transition
                                duration-200
                                disabled:bg-gray-100
                                disabled:text-gray-500
                                disabled:border-gray-400
                            "
                        >
                            Submit plaza
                        </button>
                    </div>
                </form>
            </div>
        </ul>
    </div>
</template>

<script>
import { PLAZAS } from '../../api-routes'
import Error from '~/components/messages/Error'

export default {
    components: {
        Error,
    },
    data() {
        return {
            plaza: {
                name: '',
                slug: '',
                description: '',
                permissions: '{}',
                isDisabled: false,
            },
            error: null,
        }
    },
    methods: {
        async plazaNew() {
            this.plaza.isDisabled = true

            // Send to server
            await this.$axios
                .plaza(PLAZAS.ALL(), {
                    name: this.plaza.name,
                    description: this.plaza.description,
                    slug: this.plaza.slug,
                    permissions: this.plaza.permissions,
                })
                .then((response) => {
                    this.$router.push(`/plazas/${response.data.slug}/`)
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

                    this.plaza.isDisabled = false
                })
        },
    },
}
</script>
