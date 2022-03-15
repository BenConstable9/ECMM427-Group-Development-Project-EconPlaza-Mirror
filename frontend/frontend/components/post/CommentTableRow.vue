<template>
    <div id="comment-info" class="flex items-center px-5 py-4">
        <comment :comment="comment" depth="1" />
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
}
</script>

<style></style>
