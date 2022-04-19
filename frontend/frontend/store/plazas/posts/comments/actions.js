import { PLAZAS } from '~/api-routes'

export default {
    emptyAllPostComments({ commit }) {
        commit('setComments', undefined)
    },
    async getCurrentPostComments(
        { state, commit },
        { page, plazaSlug, postID }
    ) {
        if (
            state.comments !== undefined &&
            state.currentPlaza === plazaSlug &&
            state.currentPost === postID &&
            state.pagination.page === page &&
            state.pagination.returnedSize === state.pagination.desiredSize &&
            state.pagination.returnedSort === state.pagination.desiredSort
        ) {
            return
        }
        await this.$axios
            .get(PLAZAS.COMMENTS(plazaSlug, postID), {
                params: {
                    page,
                    page_size: state.pagination.desiredSize,
                    ordering: state.pagination.desiredSort,
                },
            })
            .then(({ data }) => {
                commit('setPagination', {
                    next: data.next,
                    previous: data.previous,
                    returnedSize: state.pagination.desiredSize,
                    returnedSort: state.pagination.desiredSort,
                })
                commit('setPage', page)
                commit('setComments', data.results)
                commit('setCurrentPost', postID)
                commit('setCurrentPlaza', plazaSlug)
            })
            .catch(() => {})
    },
}
