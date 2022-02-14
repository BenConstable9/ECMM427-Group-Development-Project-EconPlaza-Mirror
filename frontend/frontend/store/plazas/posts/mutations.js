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

        // Filter all of the posts and update this one accordingly
        const post = state.posts.find(
            (post) => post.id === state.currentPost.id
        )

        post.replies += 1
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
}
