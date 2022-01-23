// All API routes defined as functions

// Plazas

export const PLAZAS = {
    ALL: () => `/v1/plazas/`,
    ONE: (slug) => `/v1/plazas/${slug}/`,
    POSTS: (slug) => `/v1/plazas/${slug}/posts/`,
    POST: (slug, post) => `/v1/plazas/${slug}/posts/${post}/`,
    COMMENTS: (slug, post) => `/v1/plazas/${slug}/posts/${post}/comments/`,
}

// Users

export const USERS = {
    ALL: () => '/v1/users/',
    ONE: (id) => `/v1/users/${id}/`,
    VOUCHES: (id) => `/v1/users/${id}/vouches/`,
    PROFILES: (id) => `/v1/users/${id}/profiles/`,
}
