function defaultState() {
    return {
        comments: undefined,
        pagination: {
            page: undefined,
            desiredSize: 10,
            returnedSize: undefined,
            next: undefined,
            previous: undefined,
        },
        currentPost: undefined,
        currentPlaza: undefined,
    }
}

export default () => {
    defaultState()
}
