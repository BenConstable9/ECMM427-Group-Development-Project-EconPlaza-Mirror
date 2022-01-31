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
    setPagination(state, { next, previous, returnedSize }) {
        state.pagination.next = next
        state.pagination.previous = previous
        state.pagination.returnedSize = returnedSize
    },
    setDesiredPaginationSize(state, size) {
        state.pagination.desiredSize = size
    },
}
