import { defaultState } from './default.js'

export default {
    setPosts(state, posts) {
        state.posts = posts
    },
    setPage(state, page) {
        state.pagination.page = page
    },
    setPagination(
        state,
        { next, previous, returnedSize, search, returnedSort }
    ) {
        state.pagination.next = next
        state.pagination.previous = previous
        state.pagination.returnedSize = returnedSize
        state.pagination.search = search
        state.pagination.returnedSort = returnedSort
    },
    setDesiredPaginationSize(state, size) {
        state.pagination.desiredSize = size
    },
    setDesiredPaginationSort(state, sort) {
        state.pagination.desiredSort = sort
    },
    resetStore(state) {
        Object.assign(state, defaultState())
    },
}
