<template>
    <div id="post-info" class="flex items-center px-5 py-4">
        <div class="flex flex-1 flex-col space-y-1">
            <h2>
                <a class="font-semibold text-primary hover:underline" href="#"
                    >Summarizing every industry job interview I have had so
                    far</a
                >
            </h2>
            <p class="flex space-x-1">
                <span class="text-sm text-gray-700"
                    >By
                    <a class="font-semibold hover:underline" href="#"
                        >LloydTao</a
                    ></span
                >
                <span class="text-sm text-gray-700 font-semibold"
                    >&middot;</span
                >
                <span class="text-sm text-gray-700"
                    >Posted {{ rand }} hours ago</span
                >
            </p>
        </div>
        <div id="replies" class="flex flex-col w-20">
            <div>
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-5 w-5 text-secondary mx-auto"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                >
                    <path
                        fill-rule="evenodd"
                        d="M7.707 3.293a1 1 0 010 1.414L5.414 7H11a7 7 0 017 7v2a1 1 0 11-2 0v-2a5 5 0 00-5-5H5.414l2.293 2.293a1 1 0 11-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z"
                        clip-rule="evenodd"
                    />
                </svg>
                <span class="flex text-xs text-gray-500 justify-center mt-1"
                    >{{ rand }} replies</span
                >
            </div>
        </div>
        <div id="views" class="flex flex-col w-20">
            <div>
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-5 w-5 text-secondary mx-auto"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                >
                    <path d="M10 12a2 2 0 100-4 2 2 0 000 4z" />
                    <path
                        fill-rule="evenodd"
                        d="M.458 10C1.732 5.943 5.522 3 10 3s8.268 2.943 9.542 7c-1.274 4.057-5.064 7-9.542 7S1.732 14.057.458 10zM14 10a4 4 0 11-8 0 4 4 0 018 0z"
                        clip-rule="evenodd"
                    />
                </svg>
                <span class="flex text-xs text-gray-500 justify-center mt-1"
                    >{{ rand }} views</span
                >
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            rand: Math.ceil(Math.random() * 24) - 1,
        }
    },
}
</script>

<style></style>
