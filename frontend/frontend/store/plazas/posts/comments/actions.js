import { PLAZAS } from '~/api-routes'

export default {
    async getCurrentPostComments(
        { state, commit },
        { page, plazaSlug, postID }
    ) {
        if (
            state.comments !== undefined &&
            state.currentPlaza === plazaSlug &&
            state.currentPost === postID &&
            state.pagination.page === page &&
            state.pagination.returnedSize === state.pagination.desiredSize
        ) {
            return
        }
        await this.$axios
            .get(PLAZAS.COMMENTS(plazaSlug, postID), {
                params: {
                    page,
                    page_size: state.pagination.desiredSize,
                },
            })
            .then(({ data }) => {
                commit('setPagination', {
                    next: data.next,
                    previous: data.previous,
                    returnedSize: state.pagination.desiredSize,
                })
                commit('setPage', page)
                commit('setComments', data.results)
                commit('setCurrentPost', postID)
                commit('setCurrentPlaza', plazaSlug)
            })
            .catch(() => {})
    },
}
