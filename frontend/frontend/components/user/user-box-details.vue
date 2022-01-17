<template>
    <div class="md:flex md:items-start bg-gray-100 px-4 py-2">
        <div class="md:flex-1">
            <ul class="list-none">
                <li>{{ username }}</li>
                <li>{{ email }}</li>
                <li>
                    Joined: {{ months[dateJoined.getMonth()] }},
                    {{ dateJoined.getFullYear() }}
                </li>
            </ul>
        </div>
        <verified v-if="verified" class="md:flex-initial" />
    </div>
</template>

<script>
import Verified from '~/components/labels/verified'

export default {
    name: 'UserBoxDetails',
    components: {
        Verified,
    },
    props: {
        email: { type: String, default: '' },
        username: { type: String, default: '' },
        dateJoined: { type: Date, default: '' },
        verified: { type: Boolean, default: false },
    },
    data() {
        return {
            months: [
                'January',
                'February',
                'March',
                'April',
                'May',
                'June',
                'July',
                'August',
                'September',
                'October',
                'November',
                'December',
            ],
        }
    },
}
</script>

<style></style>
