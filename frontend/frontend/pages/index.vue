<template>
  <main>
    <div class="container mx-auto">
      <div class="bg-gray-50 px-5 mx-auto">
        <div id="title">
          <div class="flex pt-8">
            <h1 class="text-xl font-semibold">General</h1>
          </div>
        </div>
        <div id="content" class="flex pt-5 pb-8">
          <div id="content-left" class="w-full lg:w-2/3 mr-2">
            <post-table />
          </div>
          <div
            id="content-left"
            class="hidden lg:flex lg:w-1/3 flex-col space-y-3 ml-2"
          >
            <about-box />
            <rules-box />
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script></script>

<style></style>
