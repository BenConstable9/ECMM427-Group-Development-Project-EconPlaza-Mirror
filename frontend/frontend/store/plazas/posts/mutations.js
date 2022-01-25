export default {
    setPosts(state, posts) {
        state.posts = posts
    },
    setCurrentPlaza(state, plaza) {
        state.currentPlaza = plaza
    },
    setCurrentPost(state, post) {
        state.currentPost = post
    },
    increaseReplyCount(state) {
        state.currentPost.replies += 1
    },
    setPage(state, page) {
        state.pagination.page = page
    },
    setPagination(state, { next, previous }) {
        state.pagination.next = next
        state.pagination.previous = previous
    },
}
