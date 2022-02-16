export default () => {
    return {
        posts: undefined,
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
