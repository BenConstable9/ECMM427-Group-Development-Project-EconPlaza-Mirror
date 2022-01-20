export default function ({ $axios }) {
    if (process.client) {
        const hostname = window.location.hostname
        if (hostname === 'localhost' || hostname === '127.0.0.1') {
            // If running locally, use local server
            $axios.defaults.baseURL = `http://${hostname}:8000`
            return
        }
        // Running in cloud, use api.hostname
        const url = `https://api.${hostname}:443`
        $axios.defaults.baseURL = url
    }
}
