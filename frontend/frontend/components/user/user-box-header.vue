<template>
    <div class="flex items-start bg-blue-600 px-4 py-2">
        <h3
            class="
                flex-1
                md:flex-none
                lg:flex-1
                text-lg
                font-semibold
                text-white
            "
        >
            {{ firstName }} {{ lastName }}
        </h3>
        <staff
            v-if="isStaff"
            class="flex-initial md:flex-none lg:flex-initial"
        />
    </div>
</template>

<script>
import Staff from '~/components/labels/staff'

export default {
    name: 'UserBoxHeader',
    components: {
        Staff,
    },
    props: {
        firstName: { type: String, default: '' },
        lastName: { type: String, default: '' },
        isStaff: { type: Boolean, default: false },
    },
}
</script>

<style></style>
