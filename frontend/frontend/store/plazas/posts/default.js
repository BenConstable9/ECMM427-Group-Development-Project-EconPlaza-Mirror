export const defaultState = () => {
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
                { key: '-id', name: 'Latest Posts' },
                { key: 'id', name: 'Oldest Posts' },
                { key: '-last_activity', name: 'Most Recent Activity' },
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
