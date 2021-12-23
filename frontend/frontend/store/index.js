export const getters = {
  isAuthenticated(state) {
    return state.auth.loggedIn
  },

  authenticatedUser(state) {
    return state.auth.user
  },
}
