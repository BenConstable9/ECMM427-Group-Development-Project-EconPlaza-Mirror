import { USERS } from '../../api-routes'

export default {
    async getAllProfiles({ state, commit }) {
        // If already loaded. Return
        if (state.allProfiles !== undefined) {
            return
        }
        // Make API Call to get plazas
        await this.$axios
            .get(USERS.PROFILES(this.getters.authenticatedUser.id))
            .then(({ data }) => {
                // Add text to the profile
                data.forEach((profile) => {
                    const identity = profile.global_anonymous
                        ? ' (Identity Hidden)'
                        : ' (Identity Public)'

                    profile.display_name += identity
                })
                // Mutate value
                commit('setProfilesList', data)
                commit('setCurrentProfile', data[0])
            })
            .catch(() => {})
    },
    getCurrentProfile({ getters }) {
        return getters.current
    },
}
