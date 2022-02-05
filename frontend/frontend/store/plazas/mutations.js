export default {
    setPlazaList(state, plazas) {
        state.allPlazas = plazas
    },
    setCurrentPlaza(state, plaza) {
        state.currentPlaza = plaza
    },
    setPage(state, page) {
        state.pagination.page = page
    },
    setPagination(state, { next, previous, returnedSize, search }) {
        state.pagination.next = next
        state.pagination.previous = previous
        state.pagination.returnedSize = returnedSize
        state.pagination.search = search
    },
    setDesiredPaginationSize(state, size) {
        state.pagination.desiredSize = size
    },
    joinCurrentPlaza(state, type) {
        state.currentPlaza.membership.member = true
        state.currentPlaza.membership.type = type
        state.currentPlaza.stats.members += 1
    },
    joinPlaza(state, { slug, type }) {
        // Filter the plaza
        const plaza = state.allPlazas.find((plaza) => plaza.slug === slug)
        plaza.membership.member = true
        plaza.membership.type = type
        plaza.stats.members += 1

        // If the current plaza is this, update it too
        if (state.currentPlaza.slug === slug) {
            state.currentPlaza.membership.member = true
            state.currentPlaza.membership.type = type
            state.currentPlaza.stats.members += 1
        }
    },
}
