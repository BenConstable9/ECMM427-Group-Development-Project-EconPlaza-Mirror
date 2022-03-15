import { defaultState } from './default.js'

export default {
    setComments(state, comments) {
        state.comments = comments
    },
    setPage(state, page) {
        state.pagination.page = page
    },
    setPagination(state, { next, previous, returnedSize }) {
        state.pagination.next = next
        state.pagination.previous = previous
        state.pagination.returnedSize = returnedSize
    },
    setDesiredPaginationSize(state, size) {
        state.pagination.desiredSize = size
    },
    setCurrentPlaza(state, plaza) {
        state.currentPlaza = plaza
    },
    setCurrentPost(state, post) {
        state.currentPost = post
    },
    resetStore(state) {
        Object.assign(state, defaultState())
    },
}
