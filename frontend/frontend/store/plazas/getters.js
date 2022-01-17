export default {
    all(state) {
        return state.all
    },
    current(state) {
        return (
            state.currentPlaza ?? {
                name: 'Undefined',
                slug: 'undefined',
                description: '',
                id: 0,
                stats: {
                    members: 0,
                    posts: 0,
                },
            }
        )
    },
}
