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
        <div class="flex flex-row border-b-2 bg-gray-50 items-center">
            <div class="py-3 px-4 m-2 mr-0 flex-grow text-l">{{ title }}</div>
            <div
                class="
                    cursor-pointer
                    py-3
                    rounded
                    transition
                    text-gray-400
                    flex
                    inline-center
                    hover:text-gray-600
                "
                @click="showMarkdownHelp = true"
            >
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-6 w-6 inline mr-1"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                >
                    <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                    />
                </svg>
                Formatting Help
            </div>
            <div
                class="cursor-pointer py-3 px-4 mx-2 rounded transition"
                :class="{
                    'text-gray-50': !showPreview,
                    'text-gray-600': showPreview,
                    'bg-primary': !showPreview,
                    'bg-gray-200': showPreview,
                }"
                @click="showPreview = false"
            >
                Editor
            </div>
            <div
                class="cursor-pointer py-3 px-4 mr-4 rounded transition"
                :class="{
                    'text-gray-50': showPreview,
                    'text-gray-600': !showPreview,
                    'bg-primary': showPreview,
                    'bg-gray-200': !showPreview,
                }"
                @click="showPreview = true"
            >
                Preview
            </div>
        </div>
        <textarea
            v-model="content"
            :disabled="disabled"
            class="
                w-full
                p-4
                text-m
                focus:outline-none
                text-gray-600
                shadow
                disabled:bg-gray-100
                disabled:text-gray-500
                disabled:border-gray-400
            "
            :class="{ hidden: showPreview }"
            type="text"
            :placeholder="placeholder"
            rows="5"
            maxlength="2800"
        >
        </textarea>
        <MarkdownViewer :class="{ hidden: !showPreview }" :content="content" />
        <MarkdownHelpPopup v-model="showMarkdownHelp"></MarkdownHelpPopup>
    </div>
</template>

<script>
import 'markdown-it-vue/dist/markdown-it-vue.css'

export default {
    name: 'Editor',
    props: {
        value: {
            type: String,
            default: '',
        },
        title: {
            type: String,
            default: 'Markdown Content',
        },
        placeholder: {
            type: String,
            default: 'Type your message here...',
        },
        disabled: {
            type: Boolean,
            default: false,
        },
    },
    data() {
        return {
            content: this.value,
            showPreview: false,
            showMarkdownHelp: false,
        }
    },
    watch: {
        value(value) {
            if (value !== this.content) {
                this.content = value
            }
        },
        content() {
            this.$emit('input', this.content)
        },
    },
}
</script>
