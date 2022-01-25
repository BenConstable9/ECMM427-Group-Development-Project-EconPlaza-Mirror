import { PLAZAS } from '~/api-routes'

export default {
    async getAllPlazaPosts({ state, commit }, { page, plazaSlug }) {
        // If already loaded. Return
        if (
            state.posts !== undefined &&
            state.currentPlaza === plazaSlug &&
            state.pagination.page === page
        ) {
            return
        }
        // Make API Call to get plazas
        await this.$axios
            .get(PLAZAS.POSTS(plazaSlug), {
                params: {
                    page,
                },
            })
            .then(({ data }) => {
                console.log(data)
                // Mutate value
                commit('setPagination', {
                    next: data.next,
                    previous: data.previous,
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
