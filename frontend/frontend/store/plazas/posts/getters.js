export default {
    posts(state) {
        return state.posts
    },
    currentPost(state) {
        return (
            state.currentPost ?? {
                title: 'Undefined',
                content: 'Undefined',
                id: 0,
                views: 0,
                replies: 0,
                profile: {
                    display_name: 'Undefined',
                },
            }
        )
    },
}
