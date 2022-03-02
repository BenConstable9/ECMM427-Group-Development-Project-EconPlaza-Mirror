<template>
    <div id="rules" class="flex">
        <ul class="flex flex-col w-full border rounded-lg overflow-hidden">
            <my-plazas-header />
            <ol v-if="plazas.length > 0" class="list-inside">
                <my-plazas-row
                    v-for="(plaza, index) in plazas"
                    :key="index"
                    :plaza="plaza"
                    :class="{
                        'bg-gray-50': index % 2,
                    }"
                />
            </ol>
            <ol v-else>
                <my-plazas-row
                    v-for="index in 3"
                    :key="index"
                    :plaza="{}"
                    :loading="true"
                    :class="{
                        'bg-gray-50': index % 2,
                    }"
                />
            </ol>
        </ul>
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
    name: 'MyPlazas',
    computed: {
        ...mapGetters({ plazas: 'plazas/myPlazas' }),
    },
    mounted() {
        this.loadMyPlazas()
    },
    methods: {
        ...mapActions({
            loadMyPlazas: 'plazas/getMyPlazas',
        }),
    },
}
</script>

<style></style>
