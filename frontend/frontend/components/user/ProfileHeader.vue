<template>
    <div id="profile" class="bg-gray-50 rounded-lg border">
        <div id="profile-header" class="flex flex-col justify-center">
            <div
                id="profile-image"
                class="flex bg-gray-200 justify-center px-5 py-5"
            >
                <div
                    class="w-24 h-24 object-cover rounded-full overflow-hidden"
                >
                    <img src="https://placekitten.com/320/320/" />
                </div>
            </div>
            <div
                id="profile-details"
                class="flex flex-col justify-center px-5 py-5"
            >
                <div class="flex-col">
                    <h1 class="text-lg text-gray-900 font-semibold text-center">
                        Lewis Lloyd
                    </h1>
                    <p class="text-gray-700 text-center">@lloyd</p>
                    <p class="text-gray-500 text-center mt-1">
                        Member since January 1 2021
                    </p>
                </div>
                <div class="flex space-x-1 justify-center mt-3">
                    <div
                        class="
                            text-sm text-gray-50
                            font-semibold
                            bg-red-500
                            rounded
                            px-3
                            py-0.5
                        "
                    >
                        Staff
                    </div>
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
            </div>
        </div>
    </div>
</template>
