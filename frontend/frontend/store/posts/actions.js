import { POSTS } from '~/api-routes'

export default {
    async getAllPosts({ state, commit }, { page, search }) {
        // If already loaded. Return
        if (
            state.posts !== undefined &&
            state.pagination.page === page &&
            state.pagination.returnedSize === state.pagination.desiredSize &&
            state.pagination.search === search
        ) {
            return
        }
        // Make API Call to get plazas
        await this.$axios
            .get(POSTS.ALL(), {
                params: {
                    page,
                    page_size: state.pagination.desiredSize,
                    search,
                },
            })
            .then(({ data }) => {
                // Mutate value
                commit('setPagination', {
                    next: data.next,
                    previous: data.previous,
                    returnedSize: state.pagination.desiredSize,
                    search,
                })
                commit('setPage', page)
                commit('setPosts', data.results)
            })
            .catch(() => {})
    },
}
