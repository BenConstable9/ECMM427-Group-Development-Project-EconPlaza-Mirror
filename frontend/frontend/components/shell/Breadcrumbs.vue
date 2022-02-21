<template>
    <div class="container mx-auto px-5 pt-5">
        <div class="border rounded-lg overflow-hidden px-5 py-3 bg-gray-50">
            <ol class="flex flex-row">
                <li class="flex-initial font-semibold mr-1">Viewing:</li>
                <li class="flex-initial font-semibold mx-1">
                    <NuxtLink to="/" class="hover:underline">
                        EconPlaza
                    </NuxtLink>
                </li>
                <li
                    v-for="(crumb, index) in crumbs"
                    :key="index"
                    class="flex-initial flex items-center"
                >
                    <span
                        ><svg
                            xmlns="http://www.w3.org/2000/svg"
                            class="h-4 w-4 inline mx-1 text-secondary"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke="currentColor"
                        >
                            <path
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="2"
                                d="M13 5l7 7-7 7M5 5l7 7-7 7"
                            /></svg
                    ></span>
                    <NuxtLink
                        :to="crumb.path"
                        class="hover:underline"
                        :class="{
                            'text-primary': index === crumbs.length - 1,
                            'font-semibold': index === crumbs.length - 1,
                            'text-gray-500': index !== crumbs.length - 1,
                        }"
                    >
                        {{ crumb.title }}
                    </NuxtLink>
                </li>
            </ol>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {}
    },
    computed: {
        crumbs() {
            const fullPath = this.$route.fullPath
            const params = fullPath.startsWith('/')
                ? fullPath.substring(1).split('/')
                : fullPath.split('/')

            if (params[params.length - 1] === '') {
                params.pop()
            }

            const crumbs = []
            let path = ''
            params.forEach((param, index) => {
                path = `${path}/${param}`
                const match = this.$router.match(path)

                if (match.name !== null) {
                    const breadcrumb =
                        match.meta.breadcrumb instanceof Function
                            ? match.meta.breadcrumb(this.$route, this.$store)
                            : match.meta.breadcrumb
                    crumbs.push({
                        title: breadcrumb,
                        ...match,
                    })
                }
            })
            return crumbs
        },
    },
}
</script>

<style></style>
