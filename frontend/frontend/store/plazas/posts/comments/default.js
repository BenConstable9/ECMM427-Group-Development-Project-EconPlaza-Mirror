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
                { key: '-id', name: 'Latest Comment' },
                { key: 'id', name: 'Oldest Comment' },
            ],
        },
        currentPost: undefined,
        currentPlaza: undefined,
    }
}
