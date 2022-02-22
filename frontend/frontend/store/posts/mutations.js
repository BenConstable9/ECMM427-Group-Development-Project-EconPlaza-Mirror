import { defaultState } from './default.js'

export default {
    setPosts(state, posts) {
        state.posts = posts
    },
    setPage(state, page) {
        state.pagination.page = page
    },
    setPagination(state, { next, previous, returnedSize, search }) {
        state.pagination.next = next
        state.pagination.previous = previous
        state.pagination.returnedSize = returnedSize
        state.pagination.search = search
    },
    setDesiredPaginationSize(state, size) {
        state.pagination.desiredSize = size
    },
    resetStore(state) {
        Object.assign(state, defaultState())
    },
}
