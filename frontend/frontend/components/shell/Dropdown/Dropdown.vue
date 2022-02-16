<template>
    <div>
        <div
            class="
                fixed
                top-0
                right-0
                z-10
                h-screen
                w-screen
                bg-black
                transition
            "
            :class="{
                'invisible opacity-0': !value,
                'visible opacity-20': value,
            }"
            @click="toggleMenu"
        ></div>
        <div
            id="dropdown"
            class="absolute w-52 right-0 top-10 z-20 transition transform"
            :class="{
                'pointer-events-none opacity-0 -translate-y-1 translate-x-2 scale-95':
                    !value,
                'pointer-events-auto opacity-100 translate-y-0 translate-x-0 scale-100':
                    value,
            }"
        >
            <div class="bg-gray-50 rounded border shadow">
                <DropdownTitle> Account </DropdownTitle>
                <NuxtLink :to="`/users/${authenticatedUser.id}`">
                    <DropdownItem @click="toggleMenu">
                        <span
                            ><svg
                                xmlns="http://www.w3.org/2000/svg"
                                class="h-5 w-5"
                                viewBox="0 0 20 20"
                                fill="currentColor"
                            >
                                <path
                                    fill-rule="evenodd"
                                    d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z"
                                    clip-rule="evenodd"
                                />
                            </svg>
                        </span>
                        <span>Profile</span>
                    </DropdownItem>
                </NuxtLink>
                <NuxtLink :to="`/users/`">
                    <DropdownItem @click="toggleMenu">
                        <span
                            ><svg
                                xmlns="http://www.w3.org/2000/svg"
                                class="h-5 w-5"
                                viewBox="0 0 20 20"
                                fill="currentColor"
                            >
                                <path
                                    d="M9 6a3 3 0 11-6 0 3 3 0 016 0zM17 6a3 3 0 11-6 0 3 3 0 016 0zM12.93 17c.046-.327.07-.66.07-1a6.97 6.97 0 00-1.5-4.33A5 5 0 0119 16v1h-6.07zM6 11a5 5 0 015 5v1H1v-1a5 5 0 015-5z"
                                />
                            </svg>
                        </span>
                        <span>EconPlaza Users</span>
                    </DropdownItem>
                </NuxtLink>
                <DropdownTitle> Plazas </DropdownTitle>
                <NuxtLink :to="`/plazas/`">
                    <DropdownItem @click="toggleMenu">
                        <span
                            ><svg
                                xmlns="http://www.w3.org/2000/svg"
                                class="h-5 w-5"
                                viewBox="0 0 20 20"
                                fill="currentColor"
                            >
                                <path
                                    d="M5 3a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2V5a2 2 0 00-2-2H5zM5 11a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2v-2a2 2 0 00-2-2H5zM11 5a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V5zM11 13a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"
                                />
                            </svg>
                        </span>
                        <span>All Plazas</span>
                    </DropdownItem>
                </NuxtLink>
                <NuxtLink v-if="authenticatedUser.verified" :to="`/create/`">
                    <DropdownItem @click="toggleMenu">
                        <span
                            ><svg
                                xmlns="http://www.w3.org/2000/svg"
                                class="h-5 w-5"
                                viewBox="0 0 20 20"
                                fill="currentColor"
                            >
                                <path
                                    d="M5 3a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2V5a2 2 0 00-2-2H5zM5 11a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2v-2a2 2 0 00-2-2H5zM11 5a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V5zM14 11a1 1 0 011 1v1h1a1 1 0 110 2h-1v1a1 1 0 11-2 0v-1h-1a1 1 0 110-2h1v-1a1 1 0 011-1z"
                                />
                            </svg>
                        </span>
                        <span>Create Plaza</span>
                    </DropdownItem>
                </NuxtLink>
                <DropdownTitle> Settings </DropdownTitle>
                <a href="#" @click="$auth.logout()">
                    <DropdownItem @click="toggleMenu">
                        <span
                            ><svg
                                xmlns="http://www.w3.org/2000/svg"
                                class="h-5 w-5"
                                viewBox="0 0 20 20"
                                fill="currentColor"
                            >
                                <path
                                    fill-rule="evenodd"
                                    d="M3 3a1 1 0 00-1 1v12a1 1 0 102 0V4a1 1 0 00-1-1zm10.293 9.293a1 1 0 001.414 1.414l3-3a1 1 0 000-1.414l-3-3a1 1 0 10-1.414 1.414L14.586 9H7a1 1 0 100 2h7.586l-1.293 1.293z"
                                    clip-rule="evenodd"
                                />
                            </svg>
                        </span>
                        <span>Log Out</span>
                    </DropdownItem>
                </a>
            </div>
        </div>
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import DropdownItem from './DropdownItem'
import DropdownTitle from './DropdownTitle'
export default {
    name: 'Dropdown',
    components: { DropdownItem, DropdownTitle },
    props: {
        value: {
            type: Boolean,
            default: false,
        },
    },
    computed: {
        ...mapGetters({
            authenticatedUser: 'authenticatedUser',
        }),
    },
    methods: {
        toggleMenu() {
            this.$emit('input', !this.value)
        },
        ...mapActions({ getAllPlazas: 'plazas/getAllPlazas' }),
    },
}
</script>

<style scoped></style>
