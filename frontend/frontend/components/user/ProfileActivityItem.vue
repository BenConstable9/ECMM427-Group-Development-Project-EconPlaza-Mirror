<template>
    <div id="activity-item" class="flex items-center justify-between px-5">
        <div class="py-5">
            <p class="text-sm text-gray-500">
                <span class="text-gray-900">{{
                    activity.profile.display_name
                }}</span>
                posted in
                <NuxtLink
                    class="text-gray-900 font-semibold"
                    :to="`/plazas/${activity.plaza.slug}/`"
                    >General</NuxtLink
                >:
            </p>
            <h2 class="border-l-2 ml-3 pl-3 mt-2">
                <NuxtLink
                    class="font-semibold text-primary hover:underline"
                    :to="`/plazas/${activity.plaza.slug}/posts/${activity.id}/`"
                    >{{ activity.title }}</NuxtLink
                >
            </h2>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        activity: {
            type: Object,
            default: () => {},
        },
    },
}
</script>
