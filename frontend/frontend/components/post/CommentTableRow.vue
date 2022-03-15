<template>
    <div id="comment-info" class="flex items-center px-5 py-4">
        <comment :comment="comment" :depth="depth" />
    </div>
</template>

<script>
export default {
    props: {
        comment: {
            type: Object,
            default: undefined,
        },
    },
    computed: {
        depth() {
            return 1
        },
    },
}
</script>

<style></style>
