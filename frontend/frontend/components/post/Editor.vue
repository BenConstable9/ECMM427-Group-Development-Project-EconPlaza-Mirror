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
        <MarkdownViewer
            :class="{ hidden: !showPreview }"
            :content="content"
            :options="options"
        />
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
