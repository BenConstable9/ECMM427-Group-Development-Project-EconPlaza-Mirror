<template>
    <div id="Posts" class="bg-gray-50 rounded-lg border overflow-hidden">
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
            <div class="flex-col divide-y px-5">
                <template v-if="false">
                    <div class="italic text-gray-600 py-3">
                        User has no activity.
                    </div>
                </template>
                <template v-else>
                    <ProfileActivityItem v-for="index in 5" :key="index" />
                </template>
            </div>
        </div>
    </div>
</template>
