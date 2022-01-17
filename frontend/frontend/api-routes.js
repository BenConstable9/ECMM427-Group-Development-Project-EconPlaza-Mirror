// All API routes defined as functions

// Plazas

export const PLAZAS = {
    ALL: () => '/v1/plazas/',
    ONE: (slug) => `/v1/plazas/${slug}/`,
    POSTS: (plaza) => `v1/plazas/${plaza}/posts/`,
}
