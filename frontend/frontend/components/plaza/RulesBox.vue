<template>
    <div id="rules" class="flex">
        <ul class="flex flex-col w-full border rounded-lg overflow-hidden">
            <rules-box-header />
            <ol class="list-decimal list-inside">
                <rules-box-row
                    v-for="i in 3"
                    :key="i"
                    :class="{ 'bg-gray-50': i % 2 }"
                />
            </ol>
        </ul>
    </div>
</template>

<script></script>

<style></style>
