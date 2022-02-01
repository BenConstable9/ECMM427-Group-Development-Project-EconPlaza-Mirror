import { PLAZAS } from '../../api-routes'

export default {
    async getAllPlazas({ state, commit }, { page, search }) {
        // If already loaded. Return
        if (
            state.allPlazas !== undefined &&
            state.pagination.page === page &&
            state.pagination.returnedSize === state.pagination.desiredSize &&
            state.pagination.search === search
        ) {
            return
        }

        // Make API Call to get plazas
        await this.$axios
            .get(PLAZAS.ALL(), {
                params: {
                    page,
                    page_size: state.pagination.desiredSize,
                    search,
                },
            })
            .then(({ data }) => {
                // Mutate value
                commit('setPlazaList', data)
                commit('setPagination', {
                    next: data.next,
                    previous: data.previous,
                    returnedSize: state.pagination.desiredSize,
                    search,
                })
                commit('setPage', page)
            })
            .catch(() => {})
    },
    async getCurrentPlaza({ getters, commit }, { plazaSlug }) {
        // Check if already current
        if (getters.currentPlaza.slug === plazaSlug) {
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
