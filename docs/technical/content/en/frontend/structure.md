---
title: Structure
description: ''
position: 220
category: Frontend
---

This is a [Nuxt](https://nuxtjs.org/) application. 

Nuxt is a framework built on top of [Vue](https://vuejs.org/), which itself is a framework for building web applications similar to [React](https://reactjs.org/) and [Angular](https://angular.io/). Nuxt is not too different from a standard Vue project, and just provides a few features such as automatic routing and component discovery. In essence, it simplifies and standardises the processes involved in developing a Vue project.

## Project structure

A Nuxt application is effectively a collection of web pages, where pages are built out of components. Most development is done through implementing pages and components. There is an additional layer called the **layout**, which wraps all pages and is cached more aggressively. This is useful for components that we display persistently, such as the navigation bar.

The official Nuxt documentation explains this hierarchy through a helpful graphic.

![](https://nuxtjs.ir/nuxt-views-schema.svg)

## Component structure

A component contains a template (HTML), styles (CSS), and JavaScript to implement its functionality. This is explained in the [official Vue documentation](https://vuejs.org/guide/essentials/component-basics.html).

The application follows the principle of component-based development:
- Components are considered as modular and independent from each other. 
- A component's script is responsible for manipulating and rendering its own template.
- Communication between components occurs through listening and responding to events.
