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
                class="cursor-pointer py-3 px-4 m-2 mr-0 rounded transition"
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
                class="cursor-pointer py-3 px-4 m-2 rounded transition"
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
            <div
                class="
                    cursor-pointer
                    py-3
                    px-3
                    mr-2
                    rounded
                    transition
                    text-gray-400
                    hover:text-gray-600
                "
                @click="showMarkdownHelp = true"
            >
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-6 w-6"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                >
                    <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M18.364 5.636l-3.536 3.536m0 5.656l3.536 3.536M9.172 9.172L5.636 5.636m3.536 9.192l-3.536 3.536M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-5 0a4 4 0 11-8 0 4 4 0 018 0z"
                    />
                </svg>
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
            default: 'Content',
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
