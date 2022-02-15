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
        <div class="flex flex-row border-b-2 bg-gray-50">
            <div class="py-3 px-4 m-2 mr-0 flex-grow text-l">
                <input
                    v-model="search.tag"
                    :disabled="disabled"
                    class="
                        w-full
                        p-4
                        text-m
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
        </div>
        <div>
            <div v-if="search.results.length > 0" class="flex">
                <div
                    v-for="result in search.results"
                    :key="result.id"
                    class="
                        px-2
                        py-1
                        bg-secondary
                        rounded-lg
                        text-xs text-white
                        flex-initial
                        mr-1
                    "
                >
                    #{{ result.name }}
                </div>
            </div>
            <div v-else>
                <p>Tag #{{ search.tag }} doesn't exist. Add as new tag?</p>
                <div
                    class="cursor-pointer py-3 px-4 m-2 mr-0 rounded transition"
                    @click="addNewTag"
                >
                    Editor
                </div>
            </div>
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
        }
    },
    mounted() {
        this.searchTag()
    },
    methods: {
        prepareTag(tag) {
            return tag.trimEnd().replace(' ', '-').replace('#', '')
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
