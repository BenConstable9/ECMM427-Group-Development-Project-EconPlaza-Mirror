export default {
    setPlazaList(state, plazas) {
        state.allPlazas = plazas
    },
    setCurrentPlaza(state, plaza) {
        state.currentPlaza = plaza
    },
    joinCurrentPlaza(state, type) {
        state.currentPlaza.membership.member = true
        state.currentPlaza.membership.type = type
        state.currentPlaza.stats.members += 1
    },
}
