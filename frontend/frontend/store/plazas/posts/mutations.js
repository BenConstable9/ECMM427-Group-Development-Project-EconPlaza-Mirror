import { defaultState } from './default.js'

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

        if (state.posts !== undefined) {
            // Increase the reply count in the list
            const post = state.posts.find(
                (post) => post.id === state.currentPost.id
            )

            if (post !== undefined) {
                post.replies += 1
            }
        }
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
    setDesiredPaginationSort(state, sort) {
        state.pagination.desiredSort = sort
    },
    resetStore(state) {
        Object.assign(state, defaultState())
    },
}
