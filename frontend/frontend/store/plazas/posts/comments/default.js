export const defaultState = () => {
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
                { key: '-id', name: 'Latest Comments' },
                { key: 'id', name: 'Oldest Comments' },
            ],
        },
        currentPost: undefined,
        currentPlaza: undefined,
    }
}
