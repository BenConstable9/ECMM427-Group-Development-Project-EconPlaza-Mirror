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
                        text-primary
                        disabled:bg-gray-100
                        disabled:text-gray-500
                        disabled:border-gray-400
                    "
                    type="text"
                    placeholder="Filter Existing Tags"
                    maxlength="32"
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
                        rounded-lg
                        bg-gray-200
                        text-xs text-gray-600
                        flex-initial
                        hover:bg-secondary hover:text-gray-50
                        mr-1
                        mb-1
                    "
                    :class="{
                        'cursor-pointer': !disabled,
                    }"
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
                        py-1
                        px-2
                        rounded-lg
                        ml-2
                        flex-initial
                        bg-primary
                        text-gray-50 text-xs
                    "
                    :class="{
                        'cursor-pointer': !disabled,
                    }"
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
                    "
                    :class="{
                        'cursor-pointer': !disabled,
                    }"
                    :data-id="result.id"
                    :data-name="result.name"
                    @click="selectTag"
                >
                    #{{ result.name }}
                </div>
            </div>
            <div v-else>Select relevant tags from the above list to add.</div>
        </div>
        {{ selected }}
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
    watch: {
        selected() {
            const tags = this.selected.map(function (i) {
                return { ID: Number(i.id) }
            })
            this.$emit('input', tags)
        },
    },
    mounted() {
        this.searchTag()
    },
    methods: {
        prepareTag(tag) {
            return tag
                .trimEnd()
                .replace(/\s/g, '-')
                .replace(/#/g, '')
                .toLowerCase()
                .replace(/[^0-9a-z-]/g, '')
        },
        selectTag(e) {
            if (!this.disabled) {
                // check if in array
                const matching = this.selected.find(
                    (tag) => tag.id === e.target.dataset.id
                )

                if (matching === undefined) {
                    this.selected.push({
                        id: e.target.dataset.id,
                        name: e.target.dataset.name,
                    })
                } else {
                    this.selected.splice(this.selected.indexOf(matching), 1)
                }
            }
        },
        async addNewTag() {
            if (!this.disabled) {
                // Send off
                const tag = this.prepareTag(this.search.tag)
                await this.$axios
                    .post(TAGS.ALL(), {
                        name: tag,
                    })
                    .then((response) => {
                        this.searchTag()

                        // Push to selected
                        this.selected.push({
                            id: String(response.data.id),
                            name: response.data.name,
                        })
                    })
                    .catch((response) => {})
            }
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
