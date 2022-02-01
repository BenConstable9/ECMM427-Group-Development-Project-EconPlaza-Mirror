import { PLAZAS } from '../../api-routes'

export default {
    async getAllProfiles({ state, commit }) {
        // If already loaded. Return
        if (state.all !== undefined) {
            return
        }
        // Make API Call to get plazas
        await this.$axios
            .get(PLAZAS.ALL())
            .then(({ data }) => {
                // Mutate value
                commit('setPlazaList', data)
            })
            .catch(() => {})
    },
    async getCurrentProfile({ getters, commit }, plazaSlug) {
        // Check if already current
        if (getters.current.id === plazaSlug) {
            return
        }
        // If plaza already in all, use that
        try {
            const current = getters.all.find(({ slug }) => slug === plazaSlug)
            commit('setCurrentPlaza', current)
        } catch {
            // Otherwise load fresh
            await this.$axios
                .get(PLAZAS.ONE(plazaSlug))
                .then(({ data }) => {
                    commit('setCurrentPlaza', data)
                })
                .catch(() => {})
        }
    },
}
