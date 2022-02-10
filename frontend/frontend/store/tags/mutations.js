export default {
    setPosts(state, posts) {
        state.posts = posts
    },
    setPage(state, page) {
        state.pagination.page = page
    },
    setTag(state, tag) {
        state.tag = tag
    },
    setPagination(state, { next, previous, returnedSize }) {
        state.pagination.next = next
        state.pagination.previous = previous
        state.pagination.returnedSize = returnedSize
    },
    setDesiredPaginationSize(state, size) {
        state.pagination.desiredSize = size
    },
}
