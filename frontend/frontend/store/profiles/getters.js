export default {
    allProfiles(state) {
        return state.allProfiles
    },
    currentProfile(state) {
        return (
            state.currentProfile ?? {
                display_name: 'Undefined',
                global_anonymous: false,
                reputation: 0,
                id: 0,
            }
        )
    },
}
