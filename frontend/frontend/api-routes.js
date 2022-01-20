// All API routes defined as functions

// Plazas

export const PLAZAS = {
    ALL: () => `/v1/plazas/`,
    ONE: (slug) => `/v1/plazas/${slug}/`,
    POSTS: (plaza) => `v1/plazas/${plaza}/posts/`,
}

// Profiles

export const USERS = {
    ALL: () => `/v1/users/`,
    ONE: (id) => `/v1/users/${id}/`,
    VOUCHES: (id) => `/v1/users/${id}/vouches/`,
}
