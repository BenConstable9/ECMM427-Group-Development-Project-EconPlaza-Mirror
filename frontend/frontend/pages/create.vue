<template>
    <main>
        <div class="container mx-auto">
            <div class="bg-gray-100 px-5 mb-5 mx-auto">
                <div id="content" class="flex space-x-5 pt-5 pb-8">
                    <div id="content-left" class="w-full lg:w-3/4">
                        <plaza-form />
                    </div>
                    <div
                        id="content-right"
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
            title: `New Plaza`,
        }
    },
}
</script>
