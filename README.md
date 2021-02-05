# Cabronis Backend <!-- omit in toc -->

- [1. Authors](#1-authors)
- [2. Setup](#2-setup)
  - [2.1 Postgres database](#21-postgres-database)
    - [2.1.1 Set your postgres config in the config.py file](#211-set-your-postgres-config-in-the-configpy-file)
    - [2.1.2 Create the migration folder with this command (only do this once)](#212-create-the-migration-folder-with-this-command-only-do-this-once)
    - [2.1.3 IMPORTANT: Do these 2 steps when you add a new models, if you modify existing models, or if the database is empty](#213-important-do-these-2-steps-when-you-add-a-new-models-if-you-modify-existing-models-or-if-the-database-is-empty)
- [3. Application](#3-application)
  - [3.1 Install the requirements](#31-install-the-requirements)
  - [3.2 Run the application](#32-run-the-application)
  - [3.3 Run the tests](#33-run-the-tests)
- [4. Project architecture](#4-project-architecture)
  - [4.1 Folder structure](#41-folder-structure)
- [5. Contributing](#5-contributing)
- [6. Authentication](#6-authentication)
- [7. Branch naming](#7-branch-naming)
- [8. Commits syntax](#8-commits-syntax)
  - [8.1 Adding code](#81-adding-code)
  - [8.2 Deleting code](#82-deleting-code)
  - [8.3 Modifying code](#83-modifying-code)
  - [8.4 Merging branches](#84-merging-branches)

## 1. Authors

- Victor Trinh - [victortrinh](https://github.com/victortrinh)

## 2. Setup

### 2.1 Postgres database

#### 2.1.1 Set your postgres config in the config.py file

#### 2.1.2 Create the migration folder with this command (only do this once)

> python manage.py db init

#### 2.1.3 IMPORTANT: Do these 2 steps when you add a new models, if you modify existing models, or if the database is empty

1- To migrate your models changes to the migrations folder

> python manage.py db migrate --message "initial db migration"

2- To migrate your changes to the database

> python manage.py db upgrade

## 3. Application

### 3.1 Install the requirements

> pip install -r requirements.txt

### 3.2 Run the application

> python manage.py run

### 3.3 Run the tests

> python manage.py test

## 4. Project architecture

### 4.1 Folder structure

```bash
├── app
│   ├── main
│   │   ├── controller
│   │   ├── model
│   │   ├── service
│   ├── ├── config.py
│   ├── test
├── manage.py
```

- The controller package will contain all of the application endpoint
- The model package will contain the database models
- The service package will contain the business logic of the application

## 5. Contributing

If you find a bug or have an idea for an improvement: Then,

- [x] Create a branch by feature and/or bug fix
- [x] Get the code
- [x] Commit and push
- [x] Create a pull request

## 6. Authentication

The application uses token based authentication using the HTTP bearer authentication scheme.
Each Create/Update/Delete request must be authenticated. The obtain an authentication token using credentials, use the Authentication endpoint (login).
To test the authentication using swagger, obtain a token and use the Authorize button on top. For the `Bearer (apiKey)` value, enter `Bearer [your token]`.
To disable the authentication **FOR DEBBUGING PURPOSE ONLY**, set the `DISABLE_AUTHENTICATION` setting to `True` in config.py.

## 7. Branch naming

| Instance        | Branch                                             | Description, Instructions, Notes                   |
| --------------- | -------------------------------------------------- | -------------------------------------------------- |
| Stable          | main                                             | Accepts merges from Development and Hotfixes       |
| Development     | dev                                                | Accepts merges from Features / Issues and Hotfixes |
| Features/Issues | feature/[Issue number]-[Short feature description] | Always branch off HEAD or dev                      |
| Hotfix          | fix/[Issue number]-[Short feature description]     | Always branch off Stable                           |

## 8. Commits syntax

### 8.1 Adding code

> \+ Added [Short Description] [Issue Number]

### 8.2 Deleting code

> \- Deleted [Short Description] [Issue Number]

### 8.3 Modifying code

> \* Changed [Short Description] [Issue Number]

### 8.4 Merging branches

> Y Merged [Short Description]
