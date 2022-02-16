<template>
    <div id="rules" class="flex">
        <ul class="flex flex-col w-full border rounded-lg overflow-hidden">
            <popular-plazas-header />
            <ol class="list-inside">
                <popular-plazas-row
                    v-for="(plaza, index) in plazas"
                    :key="plaza.plaza__name"
                    :name="plaza.plaza__name"
                    :slug="plaza.plaza__slug"
                    :class="{ 'bg-gray-50': index % 2 }"
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
            this.plazas = response.data.slice(0, 5)
        },
    },
}
</script>

<style></style>
