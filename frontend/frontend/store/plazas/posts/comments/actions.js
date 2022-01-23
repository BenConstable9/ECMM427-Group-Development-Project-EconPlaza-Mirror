import { PLAZAS } from '~/api-routes'

export default {
    async getCurrentPostComments({ getters, commit }, { plazaSlug, postID }) {
        await this.$axios
            .get(PLAZAS.COMMENTS(plazaSlug, postID))
            .then(({ data }) => {
                commit('setComments', data.results)
            })
            .catch(() => {})
    },
}
