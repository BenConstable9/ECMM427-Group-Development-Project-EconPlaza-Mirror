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
                commit('setPosts', data)
                commit('setCurrentPlaza', plazaSlug)
            })
            .catch(() => {})
    },
}
