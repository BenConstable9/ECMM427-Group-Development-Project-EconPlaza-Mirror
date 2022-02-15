<template>
    <div
        class="
            w-full
            bg-white
            border border-gray-200
            rounded-lg
            overflow-hidden
            flex flex-col
        "
    >
        <div class="border-b-2 bg-gray-50">
            <div class="py-3 px-4">
                <input
                    v-model="search.tag"
                    :disabled="disabled"
                    class="
                        w-full
                        p-2
                        text-sm
                        bg-white
                        focus:outline-none
                        border border-gray-200
                        rounded-lg
                        text-blue-600
                        disabled:bg-gray-100
                        disabled:text-gray-500
                        disabled:border-gray-400
                    "
                    type="text"
                    placeholder="Filter Existing Tags"
                    @keyup="searchTag"
                />
            </div>
            <div
                v-if="search.results.length > 0"
                class="flex flex-wrap pb-2 px-4"
            >
                <div
                    v-for="result in search.results"
                    :key="result.id"
                    class="
                        px-2
                        py-1
                        bg-gray-200
                        rounded-lg
                        text-xs text-gray-600
                        flex-initial
                        mr-1
                        mb-1
                        cursor-pointer
                    "
                    :data-id="result.id"
                    :data-name="result.name"
                    @click="selectTag"
                >
                    #{{ result.name }}
                </div>
            </div>
            <div v-else class="pb-2 px-4 flex">
                <div class="flex-initial">
                    Tag #{{ prepareTag(search.tag) }} doesn't exist.
                </div>
                <div
                    class="
                        cursor-pointer
                        py-1
                        px-2
                        rounded
                        ml-2
                        flex-initial
                        bg-primary
                        text-gray-50 text-xs
                    "
                    @click="addNewTag"
                >
                    Add As New Tag
                </div>
            </div>
        </div>
        <div class="py-3 px-4">
            <div v-if="selected.length > 0" class="flex flex-wrap">
                <div
                    v-for="result in selected"
                    :key="result.id"
                    class="
                        px-2
                        py-1
                        bg-secondary
                        rounded-lg
                        text-xs text-white
                        flex-initial
                        mr-1
                        mb-1
                        cursor-pointer
                    "
                    :data-id="result.id"
                    :data-name="result.name"
                    @click="selectTag"
                >
                    #{{ result.name }}
                </div>
            </div>
            <div v-else>Select relevant tags from the above list to add.</div>
        </div>
    </div>
</template>

<script>
import { TAGS } from '../../api-routes'

export default {
    name: 'Tags',
    props: {
        disabled: {
            type: Boolean,
            default: false,
        },
    },
    data() {
        return {
            search: {
                tag: '',
                results: {},
            },
            selected: [],
        }
    },
    mounted() {
        this.searchTag()
    },
    methods: {
        prepareTag(tag) {
            return tag.trimEnd().replace(/\s/g, '-').replace(/#/g, '')
        },
        checkIfSelected(id) {
            const matching = this.selected.find((tag) => tag.id === id)

            if (matching === undefined) {
                return false
            } else {
                return true
            }
        },
        selectTag(e) {
            // check if in array
            const matching = this.checkIfSelected(e.target.dataset.id)

            if (matching === false) {
                this.selected.push({
                    id: e.target.dataset.id,
                    name: e.target.dataset.name,
                })
            } else {
                this.selected.splice(this.selected.indexOf(matching), 1)
            }
        },
        async addNewTag() {
            // Send off
            const tag = this.prepareTag(this.search.tag)
            await this.$axios
                .post(TAGS.ALL(), {
                    name: tag,
                })
                .then((response) => {
                    this.searchTag()
                })
                .catch((response) => {})
        },
        async searchTag() {
            // Send off to server
            const search = this.prepareTag(this.search.tag)
            await this.$axios
                .get(TAGS.ALL(), {
                    params: {
                        search,
                    },
                })
                .then(({ data }) => {
                    this.search.results = data.results
                })
        },
    },
}
</script>
