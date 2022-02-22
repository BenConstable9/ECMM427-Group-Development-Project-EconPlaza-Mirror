export default () => {
    return {
        comments: undefined,
        pagination: {
            page: undefined,
            desiredSort: 'id',
            desiredSize: 10,
            returnedSize: undefined,
            returnedSort: undefined,
            next: undefined,
            previous: undefined,
            sortOptions: [
                { key: '-id', name: 'Newest' },
                { key: 'id', name: 'Oldest' },
            ],
        },
        currentPost: undefined,
        currentPlaza: undefined,
    }
}
