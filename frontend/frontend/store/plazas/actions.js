import { PLAZAS } from '../../api-routes'

export default {
    emptyAllPlazas({ commit }) {
        commit('setPlazaList', undefined)
    },
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
                commit('setPlazaList', data.results)
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
    async joinPlaza({ commit }, { plazaSlug }) {
        const memberType = 'MB'

        // Send to server
        await this.$axios
            .post(PLAZAS.MEMBERSHIP(plazaSlug), {
                plaza: plazaSlug,
                member_type: memberType,
            })
            .then(() => {
                commit('setPlazaMembership', {
                    slug: plazaSlug,
                    type: memberType,
                })
            })
            .catch(() => {})
    },
    async getMyPlazas({ state, commit }) {
        console.log('Hello')
        if (
            state.myPlazas.last_updated === undefined ||
            Date.now() - state.myPlazas.last_updated > 60 * 1000
        ) {
            // Update date if it is too old (over 1 minute) or if it doesn't exist
            commit('setMyPlazas', { data: [], last_updated: Date.now() })
            await this.$axios
                .get(PLAZAS.MY())
                .then(({ data }) => {
                    commit('setMyPlazas', {
                        data,
                        last_updated: Date.now(),
                    })
                })
                .catch(() => {})
        }
    },
}
