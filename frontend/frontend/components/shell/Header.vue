<template>
  <header>
    <nav id="navbar" class="bg-blue-100">
      <div class="container mx-auto px-5">
        <div id="links" class="flex items-center space-x-8 py-3">
          <ul class="flex flex-1">
            <li class="text-xl text-gray-900">EconPlaza</li>
          </ul>
          <ul class="flex space-x-8">
            <li>
              <a class="text-gray-900 hover:underline" href="#">Log in</a>
            </li>
            <li>
              <a class="text-gray-900 hover:underline" href="#">Sign up</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <nav id="plazas" class="bg-blue-50">
      <div class="container mx-auto px-5">
        <div id="links" class="flex space-x-8 py-2">
          <ul class="flex flex-1 space-x-2">
            <header-plaza-button plazaName="Home" />
            <header-plaza-button plazaName="General" />
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
import HeaderPlazaButton from './HeaderPlazaButton.vue'
export default {
  components: { HeaderPlazaButton },
}
</script>

<style></style>
