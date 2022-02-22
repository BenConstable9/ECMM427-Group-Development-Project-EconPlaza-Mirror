function defaultState() {
    return {
        posts: undefined,
        tag: undefined,
        pagination: {
            page: undefined,
            desiredSize: 10,
            returnedSize: undefined,
            next: undefined,
            previous: undefined,
            search: '',
        },
    }
}

export default () => {
    defaultState()
}
