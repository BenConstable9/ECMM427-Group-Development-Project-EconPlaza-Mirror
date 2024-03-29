export default {
    allPlazas(state) {
        return state.allPlazas
    },
    pagination(state) {
        return state.pagination
    },
    currentPlaza(state) {
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
                membership: {
                    member: false,
                    type: null,
                },
                tags: {},
            }
        )
    },
    myPlazas(state) {
        return state.myPlazas.data
    },
}
