<template>
    <div>
        <ul
            class="
                w-full
                border
                rounded-r-2xl rounded-b-2xl
                overflow-hidden
                shadow-md
            "
        >
            <plaza-box-header :name="plaza.name" />
            <plaza-box-details
                :members="plaza.stats.members"
                :posts="plaza.stats.posts"
                :date-created="new Date(plaza.created_at)"
                :description="plaza.description"
            />
        </ul>
    </div>
</template>

<script>
export default {
    name: 'PlazaBox',
    props: { plaza: { type: Object, default: null } },
}
</script>

<style></style>
