export default {
    all(state) {
        return state.all
    },
    current(state) {
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
