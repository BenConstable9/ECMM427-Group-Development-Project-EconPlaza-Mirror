// All API routes defined as functions

// Plazas

export const PLAZAS = {
  ALL: () => '/v1/plazas/',
  ONE: (slug) => `/v1/plazas/${slug}/`,
}

// Profiles

export const PROFILES = {
  ALL: () => '/v1/accounts/profiles/',
  ONE: (id) => `/v1/accounts/profiles/${id}/`,
}
