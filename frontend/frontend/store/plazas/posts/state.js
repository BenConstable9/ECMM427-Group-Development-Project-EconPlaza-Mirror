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
                { key: '-last_activity', name: 'Newest Activity' },
                { key: 'last_activity', name: 'Oldest Activity' },
                { key: '-views', name: 'Most Views' },
                { key: 'views', name: 'Least Views' },
                { key: '-replies', name: 'Most Replies' },
                { key: 'replies', name: 'Least Replies' },
            ],
        },
        currentPost: undefined,
        currentPlaza: undefined,
    }
}
