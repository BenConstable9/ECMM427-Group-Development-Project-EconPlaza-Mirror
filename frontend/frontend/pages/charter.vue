<template>
    <main>
        <div class="container mx-auto">
            <div class="bg-gray-100 px-5 mb-5 mx-auto">
                <div id="content" class="flex space-x-5 pt-5 pb-8">
                    <div id="content-left" class="w-full lg:w-3/4">
                        <div id="feed" class="flex">
                            <ul
                                class="
                                    flex flex-col
                                    w-full
                                    border
                                    rounded-lg
                                    overflow-hidden
                                "
                            >
                                <div
                                    id="charter-heading"
                                    class="
                                        flex
                                        space-x-3
                                        items-center
                                        bg-primary
                                        px-5
                                        py-3
                                    "
                                >
                                    <div id="title" class="flex-1">
                                        <div class="flex flex-col space-y-1">
                                            <h1
                                                class="
                                                    text-gray-50 text-xl
                                                    font-semibold
                                                "
                                            >
                                                EconPlaza Community Charter
                                            </h1>
                                        </div>
                                    </div>
                                </div>
                                <div
                                    id="charter-info"
                                    class="flex items-center px-5 py-4 bg-white"
                                >
                                    By joining EconPlaza, I ....
                                </div>
                            </ul>
                        </div>
                    </div>
                    <div
                        id="content-left"
                        class="hidden lg:flex lg:w-1/4 flex-col space-y-5"
                    >
                        <my-plazas />
                        <my-bookmarks />
                        <popular-plazas />
                    </div>
                </div>
            </div>
        </div>
    </main>
</template>

<script>
export default {
    head() {
        return {
            title: 'Community Charter',
        }
    },
}
</script>

<style></style>
