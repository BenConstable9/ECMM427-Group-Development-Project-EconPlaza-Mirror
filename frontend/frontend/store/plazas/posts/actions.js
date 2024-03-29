import { PLAZAS } from '~/api-routes'

export default {
    emptyAllPlazaPosts({ commit }) {
        commit('setPosts', undefined)
    },
    async getAllPlazaPosts({ state, commit }, { page, plazaSlug }) {
        // If already loaded. Return
        if (
            state.posts !== undefined &&
            state.currentPlaza === plazaSlug &&
            state.pagination.page === page &&
            state.pagination.returnedSize === state.pagination.desiredSize &&
            state.pagination.returnedSort === state.pagination.desiredSort
        ) {
            return
        }
        // Make API Call to get plazas
        await this.$axios
            .get(PLAZAS.POSTS(plazaSlug), {
                params: {
                    page,
                    page_size: state.pagination.desiredSize,
                    ordering: state.pagination.desiredSort,
                },
            })
            .then(({ data }) => {
                // Mutate value
                commit('setPagination', {
                    next: data.next,
                    previous: data.previous,
                    returnedSize: state.pagination.desiredSize,
                    returnedSort: state.pagination.desiredSort,
                })
                commit('setPage', page)
                commit('setPosts', data.results)
                commit('setCurrentPlaza', plazaSlug)
            })
            .catch(() => {})
    },
    async getCurrentPost({ getters, commit }, { plazaSlug, postID }) {
        // Check if already current
        if (getters.currentPost.id === postID) {
            return
        }
        // If post already in all, use that
        const current = getters.posts.find(({ id }) => id === postID)

        if (current !== undefined) {
            commit('setCurrentPost', current)
        } else {
            // Otherwise load fresh
            await this.$axios
                .get(PLAZAS.POST(plazaSlug, postID))
                .then(({ data }) => {
                    commit('setCurrentPost', data)
                })
                .catch(() => {})
        }
    },
}
