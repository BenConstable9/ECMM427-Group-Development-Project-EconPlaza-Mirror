import { defaultState } from './default.js'

export default {
    setProfilesList(state, profiles) {
        state.allProfiles = profiles
    },
    setCurrentProfile(state, profile) {
        state.currentProfile = profile
    },
    resetStore(state) {
        Object.assign(state, defaultState())
    },
}
