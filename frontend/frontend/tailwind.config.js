module.exports = {
    content: [
        './components/**/*.{js,vue,ts}',
        './layouts/**/*.vue',
        './pages/**/*.vue',
        './plugins/**/*.{js,ts}',
        './nuxt.config.{js,ts}',
    ],
    purge: [],
    darkMode: false, // or 'media' or 'class'
    theme: {
        extend: {
            colors: { primary: '#46B1C9', secondary: '#84C0C6' },
        },
    },
    variants: {
        backgroundColor: ({ after }) => after(['disabled']),
        textColor: ({ after }) => after(['disabled']),
        borderColor: ({ after }) => after(['disabled']),
        extend: {},
    },
    plugins: [],
}
