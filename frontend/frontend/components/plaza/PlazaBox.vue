<template>
    <div>
        <ul class="w-full border rounded-lg overflow-hidden">
            <plaza-box-header
                :slug="plaza.slug"
                :name="plaza.name"
                :is-member="plaza.membership.member"
            />
            <plaza-box-details
                :date-created="new Date(plaza.created_at)"
                :description="plaza.description"
            />
            <plaza-box-stats
                :members="plaza.stats.members"
                :posts="plaza.stats.posts"
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
