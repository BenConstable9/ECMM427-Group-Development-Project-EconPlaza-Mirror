<template>
    <markdown-it-vue
        class="md-body p-5"
        :content="content"
        :options="options"
    />
</template>

<script>
export default {
    name: 'MarkdownViewer',
    props: {
        content: {
            type: String,
            default: '',
        },
    },
    data() {
        return {
            options: {
                markdownIt: {
                    linkify: true,
                },
                linkAttributes: {
                    attrs: {
                        target: '_blank',
                        rel: 'noopener',
                    },
                },
                katex: {
                    throwOnError: false,
                    errorColor: '#cc0000',
                },
            },
        }
    },
}
</script>

<style scoped></style>
