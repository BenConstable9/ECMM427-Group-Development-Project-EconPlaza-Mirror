<template>
    <div id="vouches" class="bg-gray-50 rounded-lg border overflow-hidden">
        <div id="vouches-details" class="flex flex-col justify-center">
            <div
                id="vouches-heading"
                class="flex space-x-3 items-center bg-primary px-5 py-3"
            >
                <div id="title" class="flex-1">
                    <div class="flex flex-col space-y-1">
                        <h1 class="text-gray-50 text-lg font-semibold">
                            Vouches
                        </h1>
                    </div>
                </div>
            </div>
            <div class="flex-col divide-y px-5 py-2">
                <div
                    id="vouch-container"
                    class="flex items-center justify-between"
                >
                    <p class="text-gray-700 py-2">Lewis Lloyd</p>
                    <div
                        class="
                            text-sm text-gray-50
                            font-semibold
                            bg-green-500
                            rounded
                            px-3
                            py-0.5
                        "
                    >
                        Verified
                    </div>
                </div>
                <div
                    id="vouch-container"
                    class="flex items-center justify-between"
                >
                    <p class="text-gray-700 py-2">Lewis Lloyd</p>
                    <div
                        class="
                            text-sm text-gray-50
                            font-semibold
                            bg-green-500
                            rounded
                            px-3
                            py-0.5
                        "
                    >
                        Verified
                    </div>
                </div>
                <div
                    id="vouch-container"
                    class="flex items-center justify-between"
                >
                    <p class="text-gray-700 py-2">Lewis Lloyd</p>
                    <div
                        class="
                            text-sm text-gray-50
                            font-semibold
                            bg-green-500
                            rounded
                            px-3
                            py-0.5
                        "
                    >
                        Verified
                    </div>
                </div>
                <div
                    id="vouch-container"
                    class="flex items-center justify-between"
                >
                    <p class="text-gray-700 py-2">Lewis Lloyd</p>
                    <Verified />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Verified from '~/components/labels/verified'

export default {
    components: {
        Verified,
    },
}
</script>
