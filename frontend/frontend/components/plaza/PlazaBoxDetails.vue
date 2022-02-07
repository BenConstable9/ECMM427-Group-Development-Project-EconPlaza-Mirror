<template>
    <div class="md:flex md:items-start bg-gray-50 px-5 py-3">
        <div class="md:flex-1">
            <ul class="list-none">
                <li>{{ description }}</li>
                <li>
                    Created: {{ months[dateCreated.getMonth()] }},
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
