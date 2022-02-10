import { POSTS } from '~/api-routes'

export default {
    async getTaggedPosts({ state, commit }, { page, tag }) {
        // If already loaded. Return
        if (
            state.posts !== undefined &&
            state.pagination.page === page &&
            state.pagination.returnedSize === state.pagination.desiredSize &&
            state.tag === tag
        ) {
            return
        }
        // Make API Call to get plazas
        await this.$axios
            .get(POSTS.ALL(), {
                params: {
                    page,
                    page_size: state.pagination.desiredSize,
                    tag,
                },
            })
            .then(({ data }) => {
                // Mutate value
                commit('setPagination', {
                    next: data.next,
                    previous: data.previous,
                    returnedSize: state.pagination.desiredSize,
                })
                commit('setPage', page)
                commit('setTag', tag)
                commit('setPosts', data.results)
            })
            .catch(() => {})
    },
}
