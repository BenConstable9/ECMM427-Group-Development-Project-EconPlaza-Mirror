<template>
    <div
        v-if="isAuthenticated"
        class="relative flex-1 max-w-lg mx-auto text-gray-600"
    >
        <form
            class="flex items-center space-x-3"
            @submit.prevent="searchPlatform"
        >
            <div id="search-dropdown">
                <select name="" id="" v-model="search.resource">
                    <option value="users">Users</option>
                    <option value="plazas">Plazas</option>
                </select>
            </div>
            <div id="search-bar" class="flex-1">
                <input
                    class="
                        min-w-full
                        border-2 border-gray-300
                        bg-white
                        h-8
                        px-4
                        rounded-full
                        text-sm
                        focus:outline-none
                    "
                    type="search"
                    name="search"
                    placeholder="Search"
                />
                <button type="submit" class="absolute right-0 top-0 mt-2 mr-4">
                    <svg
                        id="Capa_1"
                        class="text-gray-600 h-4 w-4 fill-current"
                        xmlns="http://www.w3.org/2000/svg"
                        xmlns:xlink="http://www.w3.org/1999/xlink"
                        version="1.1"
                        x="0px"
                        y="0px"
                        viewBox="0 0 56.966 56.966"
                        style="enable-background: new 0 0 56.966 56.966"
                        xml:space="preserve"
                        width="512px"
                        height="512px"
                    >
                        <path
                            d="M55.146,51.887L41.588,37.786c3.486-4.144,5.396-9.358,5.396-14.786c0-12.682-10.318-23-23-23s-23,10.318-23,23  s10.318,23,23,23c4.761,0,9.298-1.436,13.177-4.162l13.661,14.208c0.571,0.593,1.339,0.92,2.162,0.92  c0.779,0,1.518-0.297,2.079-0.837C56.255,54.982,56.293,53.08,55.146,51.887z M23.984,6c9.374,0,17,7.626,17,17s-7.626,17-17,17  s-17-7.626-17-17S14.61,6,23.984,6z"
                        />
                    </svg>
                </button>
            </div>
        </form>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
    data() {
        return {
            search: {
                resource: 'plazas',
                term: '',
            },
        }
    },
    computed: {
        ...mapGetters(['isAuthenticated', 'authenticatedUser']),
    },
    methods: {
        searchPlatform() {
            // Take the search and then direct to correct page
            if (this.search.term.length > 0) {
                const url = `/${this.search.resource}/?search=${this.search.term}`

                this.$router.push(url)
            }
        },
    },
}
</script>
