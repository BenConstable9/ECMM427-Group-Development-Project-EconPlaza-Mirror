import Vue from 'vue'
import Router from 'vue-router'

import Home from './pages/index'
import Login from './pages/login'
import Register from './pages/register'
import Charter from './pages/charter'
import Privacy from './pages/privacy'
import Posts from './pages/posts'
import Tag from './pages/tags/_tag'
import Users from './pages/users/index'
import User from './pages/users/_id/index'
import Plazas from './pages/plazas/index'
import Plaza from './pages/plazas/_plazas/index'
import CreatePlaza from './pages/create'
import CreatePost from './pages/plazas/_plazas/create'
import PlazaPost from './pages/plazas/_plazas/posts/_id'

Vue.use(Router)

export function createRouter(
    ssrContext,
    createDefaultRouter,
    routerOptions,
    config,
    store
) {
    return new Router({
        mode: 'history',
        routes: [
            {
                path: '/',
                component: Home,
                meta: {
                    breadcrumb: 'Home',
                },
            },
            {
                path: '/plazas',
                component: Plazas,
                meta: {
                    breadcrumb: 'Plazas',
                },
            },
            {
                path: '/create',
                component: CreatePlaza,
                meta: {
                    breadcrumb: 'Create Plaza',
                },
            },
            {
                path: '/plazas/:plazas',
                component: Plaza,
                meta: {
                    breadcrumb: (route, store) =>
                        store.getters['plazas/currentPlaza'].name,
                },
            },
            {
                path: '/plazas/:plazas/posts/:id',
                component: PlazaPost,
                meta: {
                    breadcrumb: (route, store) =>
                        store.getters['plazas/posts/currentPost'].title,
                },
            },
            {
                path: '/plazas/:plazas/create',
                component: CreatePost,
                meta: {
                    breadcrumb: 'Create Post',
                },
            },
            {
                path: '/login',
                component: Login,
                meta: {
                    breadcrumb: 'Login',
                },
            },
            {
                path: '/register',
                component: Register,
                meta: {
                    breadcrumb: 'Register',
                },
            },
            {
                path: '/charter',
                component: Charter,
                meta: {
                    breadcrumb: 'Community Charter',
                },
            },
            {
                path: '/privacy',
                component: Privacy,
                meta: {
                    breadcrumb: 'Privacy Policy',
                },
            },
            {
                path: '/tags/:tag',
                component: Tag,
                meta: {
                    breadcrumb: (route, store) => route.params.tag,
                },
            },
            {
                path: '/posts',
                component: Posts,
                meta: {
                    breadcrumb: 'All Posts',
                },
            },
            {
                path: '/users',
                component: Users,
                meta: {
                    breadcrumb: 'All Users',
                },
            },
            {
                path: '/users/:id',
                component: User,
                meta: {
                    breadcrumb: (route, store) => route.params.id,
                },
            },
        ],
    })
}
