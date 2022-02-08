<template>
    <div class="flex bg-gray-100 px-5 py-3">
        <div class="flex-1 text-gray-900">
            <p class="text-sm">Members</p>
            <p>{{ members }}</p>
        </div>
        <div class="flex-1 text-gray-900">
            <p class="text-sm">Posts</p>
            <p>{{ posts }}</p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'PlazaBoxStats',
    props: {
        members: { type: Number, default: 0 },
        posts: { type: Number, default: 0 },
    },
}
</script>

<style></style>
