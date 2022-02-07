<template>
    <div>
        <div class="flex flex-col w-full border rounded-lg overflow-hidden">
            <plaza-box-header
                :slug="plaza.slug"
                :name="plaza.name"
                :is-member="plaza.membership.member"
            />
            <plaza-box-details :description="plaza.description" />
            <plaza-box-stats
                :members="plaza.stats.members"
                :posts="plaza.stats.posts"
            />
        </div>
    </div>
</template>

<script>
export default {
    name: 'PlazaBox',
    props: { plaza: { type: Object, default: null } },
}
</script>

<style></style>
