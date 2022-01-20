export default {
    // Target: https://go.nuxtjs.dev/config-target
    target: 'static',

    // Global page headers: https://go.nuxtjs.dev/config-head
    head: {
        title: 'frontend',
        meta: [
            { charset: 'utf-8' },
            {
                name: 'viewport',
                content: 'width=device-width, initial-scale=1',
            },
            { hid: 'description', name: 'description', content: '' },
            { name: 'format-detection', content: 'telephone=no' },
        ],
        link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
    },

    // Global CSS: https://go.nuxtjs.dev/config-css
    css: [],

    // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
    plugins: ['~/plugins/axios'],

    // Auto import components: https://go.nuxtjs.dev/config-components
    components: [
        '~/components/home',
        '~/components/plaza',
        '~/components/post',
        '~/components/shell',
    ],

    // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
    buildModules: [
        // https://go.nuxtjs.dev/eslint
        '@nuxtjs/eslint-module',
        // https://go.nuxtjs.dev/tailwindcss
        '@nuxtjs/tailwindcss',
    ],

    // Modules: https://go.nuxtjs.dev/config-modules
    modules: [
        // https://go.nuxtjs.dev/axios
        '@nuxtjs/axios',
        // https://go.nuxtjs.dev/pwa
        '@nuxtjs/pwa',
        '@nuxtjs/auth-next',
        // Proxy is needed for the API calls
        '@nuxtjs/proxy',
    ],

    // Axios module configuration: https://go.nuxtjs.dev/config-axios
    axios: {
        retry: { retries: 3 },
        prefix: '/api',
        baseUrl:
            process.env.NODE_ENV === 'production'
                ? `https://api.econplaza.bebbo.link/`
                : 'http://localhost:8000/',
        proxy: false,
    },

    // PWA module configuration: https://go.nuxtjs.dev/pwa
    pwa: {
        manifest: {
            lang: 'en',
        },
    },

    // Build Configuration: https://go.nuxtjs.dev/config-build
    build: {},

    // Force all pages to go through authentication
    router: {
        middleware: ['auth'],
    },

    auth: {
        redirect: {
            login: '/login',
            logout: '/login',
            home: '/',
        },
        strategies: {
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
                    logout: false,
                    user: { url: '/v1/accounts/user/', method: 'get' },
                    refresh: { url: '/v1/auth/refresh/', method: 'post' },
                },
            },
        },
    },
}
