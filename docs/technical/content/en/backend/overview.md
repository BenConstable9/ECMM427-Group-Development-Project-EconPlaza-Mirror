---
title: Overview
description: ''
position: 200
category: Backend
---

This subset documents the backend infrastructure which powers the API for Econ Plaza. A complete API specification can be found at: [https://api.econplaza.bebbo.link/docs].

The API is powered by Django Rest Framework which uses the Django Framework to make easily creatable APIs. [https://www.django-rest-framework.org/]

## Directory structure

The API is split into four sub-applications:

* **accounts** for all end points related to user management including vouching.
* **labels** for all end points on adding labels to a user.
* **plazas** for end points related to posting and comments.
* **reports** for the community moderation system.

Common code is located in the **utils** directory to avoid repetition.

Within each directory, the code is a standard Django application. More details can be found at: [https://docs.djangoproject.com/en/4.0/intro/overview/]