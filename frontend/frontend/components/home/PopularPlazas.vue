<template>
    <div id="rules" class="flex">
        <ul class="flex flex-col w-full border rounded-lg overflow-hidden">
            <popular-plazas-header />
            <ol class="list-inside">
                <popular-plazas-row
                    v-for="plaza in plazas"
                    :key="plaza.plaza__name"
                    :title="plaza.plaza__name"
                    :slug="plaza.plaza__slug"
                />
            </ol>
        </ul>
    </div>
</template>

<script>
import { PLAZAS } from '../../api-routes'

export default {
    data() {
        return {
            plazas: [],
        }
    },
    mounted() {
        this.getPlazas()
    },
    methods: {
        async getPlazas() {
            const response = await this.$axios.get(PLAZAS.POPULAR())
            this.plazas = response.data
        },
    },
}
</script>

<style></style>
