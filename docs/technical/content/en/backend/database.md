---
title: Database
description: ''
position: 230
category: Backend
---

The database within EconPlaza is powered through PostgresSQL. As Django has a complete database model system, no SQL needs to be written as part of the development process.

A complete entity relationship diagram can be found at: [https://git.exeter.ac.uk/ab1185/2021-ecmm427-project-02/-/blob/master/backend/docs/EconPlaza.svg]

All database models can be found in each application directory within the subsequent **models** folder. After changing a model, run:

```bash
$ python manage.py createmigrations
$ python manage.py migrate
```
