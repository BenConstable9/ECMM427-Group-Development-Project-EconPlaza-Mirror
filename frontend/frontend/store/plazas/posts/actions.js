import { PLAZAS } from '~/api-routes'

export default {
    async getAllPlazaPosts({ state, commit }, plazaSlug) {
        // If already loaded. Return
        if (state.posts !== undefined && state.currentPlaza === plazaSlug) {
            return
        }
        // Make API Call to get plazas
        await this.$axios
            .get(PLAZAS.POSTS(plazaSlug))
            .then(({ data }) => {
                // Mutate value
                commit('setPosts', data.results)
                commit('setCurrentPlaza', plazaSlug)
            })
            .catch(() => {})
    },
    async getCurrentPost({ getters, commit }, { plazaSlug, postID }) {
        // Check if already current
        if (getters.current.id === postID) {
            return
        }
        console.log(postID)
        // If post already in all, use that
        try {
            const current = getters.posts.find(({ id }) => id === postID)
            commit('setCurrentPost', current)
        } catch {
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
