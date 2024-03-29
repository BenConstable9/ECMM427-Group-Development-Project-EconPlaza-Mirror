export default {
    // Target: https://go.nuxtjs.dev/config-target
    target: 'static',

    generate: {
        fallback: 'index.html',
    },

    // Global page headers: https://go.nuxtjs.dev/config-head
    head: {
        title: '',
        titleTemplate: (title) => {
            return title ? `${title} | EconPlaza` : 'EconPlaza'
        },
        meta: [
            { charset: 'utf-8' },
            {
                name: 'viewport',
                content: 'width=device-width, initial-scale=1',
            },
            { hid: 'description', name: 'description', content: '' },
            { name: 'format-detection', content: 'telephone=no' },
        ],
        link: [
            { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
            {
                rel: 'stylesheet',
                type: 'text/css',
                href: 'https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.5.1/katex.min.css',
            },
        ],
    },

    // Global CSS: https://go.nuxtjs.dev/config-css
    css: [],

    // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
    plugins: [
        '~/plugins/axios',
        // Markdown Editor
        { src: '~/plugins/markdown-it.client.js', mode: 'client' },
    ],

    // Auto import components: https://go.nuxtjs.dev/config-components
    components: [
        '~/components/home',
        '~/components/plaza',
        '~/components/post',
        '~/components/shell',
        '~/components/user',
    ],

    // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
    buildModules: [
        // https://go.nuxtjs.dev/eslint
        '@nuxtjs/eslint-module',
        // https://go.nuxtjs.dev/tailwindcss
        '@nuxtjs/tailwindcss',
        [
            '@nuxtjs/router',
            {
                filename: 'router.js',
            },
        ],
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
        '@nuxtjs/recaptcha',
    ],

    recaptcha: {
        /* reCAPTCHA options */
        hideBadge: false, // Hide badge element (v3 & v2 via size=invisible)
        language: 'english', // Recaptcha language (v2)
        siteKey: '6LfbGWMeAAAAAFkxGJoH0Zw07lT0_nmdFA4zWQzX', // Site key for requests
        version: 2, // Version
        size: 'normal', // Size: 'compact', 'normal', 'invisible' (v2)
    },

    publicRuntimeConfig: {
        recaptcha: {
            /* reCAPTCHA options for production */
            siteKey:
                process.env.RECAPTCHA_SITE_KEY ||
                '6LfbGWMeAAAAAFkxGJoH0Zw07lT0_nmdFA4zWQzX',
        },
    },

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
            home: false,
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
                    user: { url: '/v1/users/me/', method: 'get' },
                    logout: false,
                    refresh: { url: '/v1/auth/refresh/', method: 'post' },
                },
            },
        },
    },
}
