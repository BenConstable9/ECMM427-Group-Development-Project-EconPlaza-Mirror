<template>
    <div id="Posts" class="rounded-lg border overflow-hidden">
        <div id="activity-details" class="flex flex-col justify-center">
            <div
                id="activity-heading"
                class="flex space-x-3 items-center bg-primary px-5 py-3"
            >
                <div id="title" class="flex-1">
                    <div class="flex flex-col space-y-1">
                        <h1 class="text-gray-50 text-lg font-semibold">
                            Recent Activity
                        </h1>
                    </div>
                </div>
            </div>
            <div class="flex-col divide-y">
                <template v-if="activities.length == 0">
                    <div class="italic text-gray-600 py-3 px-5">
                        User has no activity.
                    </div>
                </template>
                <template v-else>
                    <ProfileActivityItem
                        v-for="(activity, index) in activities"
                        :key="activity.id"
                        :activity="activity"
                        :class="{ 'bg-gray-50': index % 2 }"
                    />
                </template>
            </div>
        </div>
    </div>
</template>

<script>
import { USERS } from '../../api-routes'

export default {
    data() {
        return {
            activities: [],
        }
    },
    async fetch() {
        const response = await this.$axios.get(
            USERS.ACTIVITY(this.$route.params.id)
        )
        this.activities = response.data
    },
}
</script>
