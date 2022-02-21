<template>
    <div id="memberships" class="bg-gray-50 rounded-lg border overflow-hidden">
        <div id="memberships-details" class="flex flex-col justify-center">
            <div
                id="memberships-heading"
                class="flex space-x-3 items-center bg-primary px-5 py-3"
            >
                <div id="title" class="flex-1">
                    <div class="flex flex-col space-y-1">
                        <h1 class="text-gray-50 text-lg font-semibold">
                            Memberships
                        </h1>
                    </div>
                </div>
            </div>
            <div class="flex-col divide-y px-5 py-2">
                <template v-if="false">
                    <div class="italic text-gray-600">
                        User has no memberships.
                    </div>
                </template>
                <template v-else>
                    <div
                        id="membership-container"
                        class="flex items-center justify-between"
                    >
                        <p class="text-gray-700 py-2">University of Exeter</p>
                    </div>
                    <div
                        id="membership-container"
                        class="flex items-center justify-between"
                    >
                        <p class="text-gray-700 py-2">General</p>
                    </div>
                    <div
                        id="membership-container"
                        class="flex items-center justify-between"
                    >
                        <p class="text-gray-700 py-2">EconPlaza News</p>
                    </div>
                    <div
                        id="membership-container"
                        class="flex items-center justify-between"
                    >
                        <p class="text-gray-700 py-2">Twitter Community</p>
                    </div>
                </template>
            </div>
        </div>
    </div>
</template>
