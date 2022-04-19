export const defaultState = () => {
    return {
        posts: undefined,
        tag: undefined,
        pagination: {
            page: undefined,
            desiredSize: 10,
            desiredSort: '-id',
            returnedSize: undefined,
            returnedSort: undefined,
            next: undefined,
            previous: undefined,
            search: '',
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
    }
}
