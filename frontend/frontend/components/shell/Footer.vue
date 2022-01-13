<template>
  <footer>
    <div id="navbar" class="bg-gray-50">
      <div class="container mx-auto px-5">
        <div id="links" class="flex space-x-8 py-5">
          <ul class="flex">
            <li class="text-sm text-gray-500">EconPlaza &copy; {{ date }}</li>
          </ul>
        </div>
    </footer>
</template>

<script>
export default {
    data() {
        return {
            date: new Date().getFullYear(),
        }
    },
}
</script>

<style></style>
