export const getters = {
    isAuthenticated(state) {
        return state.auth.loggedIn
    },

    authenticatedUser(state) {
        return state.auth.user
    },
}

export const actions = {
    resetStore({ dispatch }) {
        dispatch('plazas/resetStore')
        dispatch('plazas/posts/resetStore')
        dispatch('plazas/posts/comments/resetStore')
        dispatch('posts/resetStore')
        dispatch('profiles/resetStore')
        dispatch('tags/resetStore')
    },
}
