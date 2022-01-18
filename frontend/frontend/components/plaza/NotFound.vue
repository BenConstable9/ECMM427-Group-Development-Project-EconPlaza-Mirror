<template>
    <div class="flex space-x-5 pt-5 pb-8">
        <div id="content-left" class="w-full lg:w-3/4">
            <h1 class="text-primary text-2xl my-10">Plaza Not Found!</h1>
            <p class="text-gray-500">
                We can't seem to find this plaza, it may have been removed or
                deleted
            </p>
            <p class="my-5">
                <NuxtLink
                    to="/"
                    class="
                        px-5
                        py-2
                        rounded-lg
                        bg-primary
                        text-gray-100
                        hover:bg-secondary
                    "
                >
                    Take Me Home
                </NuxtLink>
            </p>
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
</template>

<script></script>

<style></style>
