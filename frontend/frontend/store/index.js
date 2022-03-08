export const getters = {
    isAuthenticated(state) {
        return state.auth.loggedIn
    },

    authenticatedUser(state) {
        return state.auth.user
    },
}

export const actions = {
    resetStore({ commit }) {
        commit('plazas/resetStore')
        commit('plazas/posts/resetStore')
        commit('plazas/posts/comments/resetStore')
        commit('posts/resetStore')
        commit('profiles/resetStore')
        commit('tags/resetStore')
    },
}
