<template>
  <div id="post-heading" class="flex space-x-3 items-center px-5 py-3">
    <form class="space-y-4 w-full" @submit.prevent="postNew">
      <div>
        <input
          v-model="post.title"
          :disabled="post.isDisabled"
          class="
            w-full
            p-4
            text-m
            bg-white
            focus:outline-none
            border border-gray-200
            rounded-r-2xl rounded-b-2xl
            text-blue-600
            shadow
            disabled:bg-gray-100 disabled:text-gray-500 disabled:border-gray-400
          "
          type="text"
          placeholder="Post Title"
          maxlength="140"
        />
      </div>
      <div>
        <textarea
          v-model="post.description"
          :disabled="post.isDisabled"
          class="
            w-full
            p-4
            text-m
            bg-white
            focus:outline-none
            border border-gray-200
            rounded-r-2xl rounded-b-2xl
            text-blue-600
            shadow
            disabled:bg-gray-100 disabled:text-gray-500 disabled:border-gray-400
          "
          type="text"
          placeholder="Post Description"
          rows="5"
          maxlength="2800"
        >
        </textarea>
      </div>
      <div>
        <button
          type="submit"
          :disabled="post.isDisabled"
          class="
            w-full
            py-4
            bg-blue-600
            hover:bg-blue-800
            rounded-r-2xl rounded-b-2xl
            text-m
            font-bold
            border border-blue-600
            text-white
            shadow
            transition
            duration-200
            disabled:bg-gray-100 disabled:text-gray-500 disabled:border-gray-400
          "
        >
          Submit Post
        </button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      post: {
        title: '',
        description: '',
        isDisabled: false,
      },
      error: null,
    }
  },
}
</script>
