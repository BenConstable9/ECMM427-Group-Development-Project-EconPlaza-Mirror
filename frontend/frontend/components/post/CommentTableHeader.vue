<template>
    <div
        id="post-heading"
        class="flex space-x-3 items-center bg-primary px-5 py-3"
    >
        <div id="title" class="flex-1">
            <div class="flex flex-col space-y-1">
                <h1 class="text-gray-50 text-xl font-semibold">Comments</h1>
            </div>
        </div>
        <pagination-size :size="pagination.preferredSize" />
        <pagination-sort
            :sort="pagination.desiredSort"
            :options="pagination.sortOptions"
        />
        <div id="views">
            <div class="rounded-full bg-gray-50 p-3">
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-5 w-5 text-primary mx-auto"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                >
                    <path
                        d="M6 10a2 2 0 11-4 0 2 2 0 014 0zM12 10a2 2 0 11-4 0 2 2 0 014 0zM16 12a2 2 0 100-4 2 2 0 000 4z"
                    />
                </svg>
            </div>
        </div>
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import PaginationSize from '~/components/helpers/PaginationSize'
import PaginationSort from '~/components/helpers/PaginationSort'

export default {
    components: {
        PaginationSize,
        PaginationSort,
    },
    data() {
        return {
            loading: false,
        }
    },
    computed: {
        ...mapGetters({
            pagination: 'plazas/posts/comments/pagination',
        }),
    },
    methods: {
        ...mapActions({
            getCurrentPostComments:
                'plazas/posts/comments/getCurrentPostComments',
        }),
    },
}
</script>
