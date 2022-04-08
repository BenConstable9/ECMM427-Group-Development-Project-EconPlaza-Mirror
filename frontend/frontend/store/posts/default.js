export const defaultState = () => {
    return {
        posts: undefined,
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
                { key: '-id', name: 'Latest Post' },
                { key: 'id', name: 'Oldest Post' },
                { key: '-last_activity', name: 'Most Recent Activity' },
                { key: '-views', name: 'Most Views' },
                { key: 'views', name: 'Least Views' },
                { key: '-replies', name: 'Most Replies' },
                { key: 'replies', name: 'Least Replies' },
            ],
        },
    }
}
