<template>
    <div id="feed" class="flex">
        <ul class="flex flex-col w-full border rounded-lg overflow-hidden">
            <feed-table-header />
            <feed-table-row
                v-for="i in 8"
                :key="i"
                :class="{ 'bg-gray-50': i % 2 }"
            />
        </ul>
    </div>
</template>

<script></script>

<style></style>
