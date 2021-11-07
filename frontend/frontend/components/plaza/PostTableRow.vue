<template>
  <div id="post-info" class="flex items-center px-3 py-2">
    <div class="mr-2">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="h-7 w-7 text-gray-300 hover:text-gray-400 cursor-pointer"
        viewBox="2 -1 20 20"
        fill="currentColor"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-8.707l-3-3a1 1 0 00-1.414 0l-3 3a1 1 0 001.414 1.414L9 9.414V13a1 1 0 102 0V9.414l1.293 1.293a1 1 0 001.414-1.414z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="flex flex-col space-y-0.5">
      <h2>
        <a class="text-sm text-blue-800 hover:underline" href="#"
          >Summarizing every industry job interview I have had so far</a
        >
      </h2>
      <p class="flex space-x-1">
        <span class="text-xs text-gray-700"
          >{{ rand }} score by
          <a class="text-xs text-blue-800 hover:underline" href="#"
            >LloydTao</a
          ></span
        >
        <span class="text-xs text-gray-700 font-semibold">&middot;</span>
        <span class="text-xs text-gray-700">{{ rand }} comments</span>
        <span class="text-xs text-gray-700 font-semibold">&middot;</span>
        <span class="text-xs text-gray-700">{{ rand }} hours ago</span>
      </p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      rand: Math.ceil(Math.random() * 24) - 1,
    }
  },
}
</script>

<style></style>
