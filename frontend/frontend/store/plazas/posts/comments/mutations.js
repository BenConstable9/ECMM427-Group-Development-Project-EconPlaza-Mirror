import { defaultState } from './default.js'

export default {
    setComments(state, comments) {
        state.comments = comments
    },
    addComment(state, comment) {
        state.comments.unshift(comment)
    },
    setPage(state, page) {
        state.pagination.page = page
    },
    setPagination(state, { next, previous, returnedSize, returnedSort }) {
        state.pagination.next = next
        state.pagination.previous = previous
        state.pagination.returnedSize = returnedSize
        state.pagination.returnedSort = returnedSort
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
    setDesiredPaginationSort(state, sort) {
        state.pagination.desiredSort = sort
    },
    resetStore(state) {
        Object.assign(state, defaultState())
    },
}
