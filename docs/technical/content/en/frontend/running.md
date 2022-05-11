---
title: Running the Frontend
description: ''
position: 210
category: Frontend
---

Make sure you have NodeJS 16.15.0 LTS installed and configured on the system.

Install and set up YARN. You can find a guide to enable it with Corepack here: [https://yarnpkg.com/getting-started/install]

Navigate to the source code directory with:

```bash
$ cd frontend
```

Install the required packages with Yarn.

```bash
$ yarn install
```

You can start the development server with:

```bash
$ yarn dev
```

If using in production, you can start without dev mode with:

```bash
$ yarn build
$ yarn start
```