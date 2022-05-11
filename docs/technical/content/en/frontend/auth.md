---
title: Authentication
description: ''
position: 240
category: Frontend
---

EconPlaza uses the standard Django Authentication system on the backend and the standard Nuxt-auth configuration on the frontend. JSON Web Tokens are used for authentication. The local strategy is configured as follows:

```js
local: {
    scheme: 'refresh',
    token: {
        property: 'access',
        maxAge: 60 * 5,
        global: true,
        type: 'Bearer',
    },
    refreshToken: {
        property: 'refresh',
        data: 'refresh',
        maxAge: 60 * 60 * 24,
    },
    user: {
        property: false,
        autoFetch: true,
    },
    endpoints: {
        login: { url: '/v1/auth/login/', method: 'post' },
        user: { url: '/v1/users/me/', method: 'get' },
        logout: false,
        refresh: { url: '/v1/auth/refresh/', method: 'post' },
    },
},
```

Each provided access token is valid for a maximum of 5 minutes to ensure a high turn over of tokens to keep the site secure. A user can authenticate with a JSON request to **/v1/auth/login/** and recieve a token back.

Additional authenticator providers can be defined within **nuxt.config.js**. More information on the different schemes that Nuxt supports can be found at: [https://auth.nuxtjs.org/]