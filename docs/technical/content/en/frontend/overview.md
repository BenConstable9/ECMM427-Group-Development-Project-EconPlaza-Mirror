---
title: Overview
description: ''
position: 200
category: Frontend
---

This subset documents the frontend wrapper for the API. The frontend is written with the Nuxt Framework.

## Directory structure

The frontend code is a standard Nuxt architecture and is split as:

* **components** Contains reusable code blocks that are used across the site.
* **layouts** contains the standard layout information.
* **pages** contains individual pages for diferent sections. These pages use the store and the defined components to present a view to the user.
* **static** a store for all static resources e.g. images.
* **store** contains all the Vuex store information. The store contains actions to get and update information in the API. More information on the store can be found at: [https://nuxtjs.org/docs/directory-structure/store/]

The following files are important:

* **api-routes.js** stores and defines the API route information.
* **nuxt.config.js** contains the system configuration for Nuxt.
* **router.js** contains the routing information which tells Nuxt how the URLs link to the pages. 

Within each directory, the code is a standard Nuxt application. More details can be found at: [https://nuxtjs.org/docs/get-started/installation]