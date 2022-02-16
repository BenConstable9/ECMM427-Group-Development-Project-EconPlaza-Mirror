<template>
    <div v-if="visible" id="popup">
        <div
            id="overlay"
            class="
                w-screen
                h-screen
                fixed
                bg-gray-500
                opacity-30
                top-0
                left-0
                right-0
            "
            @click="$emit('closePopup', false)"
        ></div>
        <div
            id="popup-container"
            class="
                fixed
                w-screen
                h-screen
                pointer-events-none
                top-0
                left-0
                right-0
                flex
                items-center
                justify-center
            "
        >
            <div
                class="
                    w-2/5
                    h-4/5
                    bg-white
                    rounded-lg
                    flex flex-col
                    pointer-events-auto
                    overflow-hidden
                "
            >
                <div class="w-full flex flex-row bg-primary items-center">
                    <div
                        class="
                            flex-grow
                            p-2
                            m-2
                            text-gray-50 text-xl
                            font-semibold
                        "
                    >
                        {{ title }}
                    </div>
                    <div
                        class="
                            p-3
                            m-3
                            cursor-pointer
                            rounded-full
                            bg-gray-50
                            text-primary
                        "
                        style="width: fit-content; height: fit-content"
                        @click="$emit('closePopup', false)"
                    >
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            class="h-5 w-5"
                            viewBox="0 0 20 20"
                            fill="currentColor"
                        >
                            <path
                                fill-rule="evenodd"
                                d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                                clip-rule="evenodd"
                            />
                        </svg>
                    </div>
                </div>
                <div class="w-full flex-grow p-3 overflow-y-auto">
                    <slot></slot>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Popup',
    props: {
        visible: {
            type: Boolean,
            required: true,
        },
        title: {
            type: String,
            default: '',
        },
    },
}
</script>

<style scoped></style>
