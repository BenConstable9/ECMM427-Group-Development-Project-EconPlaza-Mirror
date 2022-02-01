<template>
    <div class="md:flex md:items-start bg-gray-100 px-4 py-2">
        <div class="md:flex-1">
            <ul class="list-none">
                <li>{{ members }}</li>
                <li>{{ posts }}</li>
                <li>{{ description }}</li>
                <li>
                    Joined: {{ months[dateCreated.getMonth()] }},
                    {{ dateCreated.getFullYear() }}
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
    name: 'PlazaBoxDetails',
    props: {
        members: { type: Number, default: 0 },
        posts: { type: Number, default: 0 },
        dateCreated: { type: Date, default: '' },
        description: { type: String, default: '' },
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
