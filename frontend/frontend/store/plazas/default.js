export const defaultState = () => {
    return {
        allPlazas: undefined,
        currentPlaza: undefined,
        pagination: {
            page: undefined,
            desiredSize: 12,
            returnedSize: undefined,
            next: undefined,
            previous: undefined,
            search: '',
        },
        myPlazas: {
            data: [],
        },
    }
}
