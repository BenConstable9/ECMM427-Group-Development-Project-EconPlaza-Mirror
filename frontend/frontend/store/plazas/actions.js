import { PLAZAS } from '../../api-routes'

export default {
  async getAllPlazas({ state, commit }) {
    // If already loaded. Return
    if (state.all !== undefined) {
      return
    }
    // Make API Call to get plazas
    await this.$axios
      .get(PLAZAS.ALL)
      .then(({ data }) => {
        // Mutate value
        commit('setPlazaList', data)
      })
      .catch(() => {})
  },
}
