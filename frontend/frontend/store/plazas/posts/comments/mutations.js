export default {
    setComments(state, comments) {
        state.comments = comments
    },
    addComment(state, comment) {
        state.comments.unshift(comment)
    },
}
