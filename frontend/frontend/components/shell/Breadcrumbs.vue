<template>
    <div class="container mx-auto px-5 pt-5">
        <div
            class="
                w-full
                border
                rounded-lg
                overflow-hidden
                px-5
                py-3
                bg-gray-50
                w-full
            "
        >
            <ol class="flex flex-row w-full">
                <li class="flex-initial font-semibold">
                    <NuxtLink to="/">
                        <span>EconPlaza</span>
                    </NuxtLink>
                    <meta property="position" content="1" />
                </li>
                <li
                    v-for="(crumb, index) in crumbs"
                    :key="index"
                    class="flex-initial mx-2"
                >
                    <NuxtLink :to="crumb.path">
                        <span>{{
                            $route.fullPath === crumb.path && title !== null
                                ? title
                                : crumb.title
                        }}</span>
                    </NuxtLink>
                    <meta property="position" :content="index + 2" />
                </li>
            </ol>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        title: {
            type: String,
            default: null,
        },
    },
    computed: {
        crumbs() {
            const fullPath = this.$route.fullPath
            const params = fullPath.startsWith('/')
                ? fullPath.substring(1).split('/')
                : fullPath.split('/')
            const crumbs = []
            let path = ''
            params.forEach((param, index) => {
                path = `${path}/${param}`
                const match = this.$router.match(path)

                if (match.name !== null) {
                    crumbs.push({
                        title: param.replace(/-/g, ' '),
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
