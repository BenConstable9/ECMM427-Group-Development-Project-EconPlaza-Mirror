---
title: Application Structure
description: ''
position: 280
category: Backend
---

Each of the four applications has a common directory structure as follows:

* **admin** Controls which of the fields will appear in the Admin interface
* **migrations** Generated database migrations to be applied.
* **models** Python classes that describe how the database should be form and the constraints on the database. The database design is created directly from these models.
* **permissions** Permission models that Django interprets to determine if a user is allowed an action or not.
* **serializers** Converts to and from JSON so that the API can interact with the Python classes. For each model, a serializer must exist to tell DRF how to interpret the JSON data.
* **signals** Automated code scripts that will fire when an event triggers them.
* **tests** Tests built using Django's standard testing framework.
* **views** A view represents an action on the API such as create or delete. Each of the views is transformed into a URL. The view defines what action must be taken and brings together all the serializer, permission and model functionality into one function.
* **viewset** A viewset is similar to a view and simply combines several different view types into a single view for quick and easy development with a CRUD model.

* **urls.py** This file defines the URL routes for the application. All new models need a URL added into here so they are detected by the main application.
