<template>
  <footer>
    <div id="navbar" class="bg-gray-100">
      <div class="container mx-auto px-5">
        <div id="links" class="flex space-x-8 py-3">
          <ul class="flex">
            <li class="text-sm">EconPlaza &copy; {{ date }}</li>
          </ul>
        </div>
      </div>
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
