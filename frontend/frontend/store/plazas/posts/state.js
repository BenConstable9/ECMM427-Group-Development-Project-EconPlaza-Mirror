export default () => {
    return {
        posts: undefined,
        pagination: {
            page: undefined,
            desiredSort: '-id',
            desiredSize: 10,
            returnedSize: undefined,
            returnedSort: undefined,
            next: undefined,
            previous: undefined,
            sortOptions: [
                { key: '-id', name: 'Newest' },
                { key: 'id', name: 'Oldest' },
                { key: '-views', name: 'Most Views' },
                { key: 'views', name: 'Least Views' },
            ],
        },
        currentPost: undefined,
        currentPlaza: undefined,
    }
}
