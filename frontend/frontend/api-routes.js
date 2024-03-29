// All API routes defined as functions

// Plazas

export const PLAZAS = {
    ALL: () => `/v1/plazas/`,
    ONE: (slug) => `/v1/plazas/${slug}/`,
    POSTS: (slug) => `/v1/plazas/${slug}/posts/`,
    POST: (slug, post) => `/v1/plazas/${slug}/posts/${post}/`,
    VIEWPOST: (slug, post) => `/v1/plazas/${slug}/posts/${post}/view/`,
    COMMENTS: (slug, post) => `/v1/plazas/${slug}/posts/${post}/comments/`,
    MEMBERSHIP: (slug) => `/v1/plazas/${slug}/membership/`,
    POPULAR: () => `/v1/plazas/?popular`,
    MY: () => `/v1/plazas/?my`,
}

// Posts

export const POSTS = {
    ALL: () => `/v1/posts/`,
}

// Tags
export const TAGS = {
    ALL: () => `/v1/tags/`,
}

// Users

export const USERS = {
    ALL: () => '/v1/users/',
    ONE: (id) => `/v1/users/${id}/`,
    VOUCHES: (id) => `/v1/users/${id}/vouches/`,
    PROFILES: (id) => `/v1/users/${id}/profiles/`,
    MEMBERSHIPS: (id) => `/v1/users/${id}/memberships/`,
    ACTIVITY: (id) => `/v1/users/${id}/activity/`,
    REGISTER: () => `/v1/users/`,
}
