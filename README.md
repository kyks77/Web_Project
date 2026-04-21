
# ProjectWeb

This project was generated using [Angular CLI](https://github.com/angular/angular-cli) version 21.2.2.

## Development server

To start a local development server, run:

```bash
ng serve
```

Once the server is running, open your browser and navigate to `http://localhost:4200/`. The application will automatically reload whenever you modify any of the source files.

## Code scaffolding

Angular CLI includes powerful code scaffolding tools. To generate a new component, run:

```bash
ng generate component component-name
```

For a complete list of available schematics (such as `components`, `directives`, or `pipes`), run:

```bash
ng generate --help
```

## Building

To build the project run:

```bash
ng build
```

This will compile your project and store the build artifacts in the `dist/` directory. By default, the production build optimizes your application for performance and speed.

## Running unit tests

To execute unit tests with the [Vitest](https://vitest.dev/) test runner, use the following command:

```bash
ng test
```

## Running end-to-end tests

For end-to-end (e2e) testing, run:

```bash
ng e2e
```

Angular CLI does not come with an end-to-end testing framework by default. You can choose one that suits your needs.

## Additional Resources

For more information on using the Angular CLI, including detailed command references, visit the [Angular CLI Overview and Command Reference](https://angular.dev/tools/cli) page.
=======
# F1 Hub Ticket Platform

Angular + Django REST university project for browsing Formula 1 teams and races, then buying tickets for selected Grand Prix weekends.

## Group Members
- Student 1 - 24B031972 Rakhymzhan Kuanysh
- Student 2 - 24B031899 Mukhtarbek Daniyal
- Student 3 - 23B031842 Akhmetzhanov Imran

## Project Idea
The application helps users:
- browse Formula 1 teams
- view race schedule and upcoming events
- log in with JWT authentication
- buy, edit, list, and cancel tickets linked to the authenticated user

## Tech Stack
- Frontend: Angular 21 standalone components
- Backend: Django 5 + Django REST Framework
- Auth: JWT via `djangorestframework-simplejwt`
- Database: SQLite

## Main Features
- Angular routing with pages for home, teams, races, tickets, and login
- Shared API service using `HttpClient`
- JWT interceptor for authenticated requests
- Ticket CRUD connected to Django REST API
- Error handling on failed API requests
- DRF function-based and class-based views
- CORS configured for Angular dev server

## Run Frontend
```bash
npm install
ng serve
```

Frontend runs on `http://localhost:4200`.

## Run Backend
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Backend runs on `http://localhost:8000`.

## API Overview
- `POST /api/auth/login/`
- `POST /api/auth/logout/`
- `GET /api/teams/`
- `GET /api/races/`
- `GET /api/races/summary/`
- `GET /api/stats/drivers/`
- `GET/POST /api/tickets/`
- `GET/PUT/DELETE /api/tickets/<id>/`

## Postman
Postman collection is included in [postman/F1Hub.postman_collection.json](/c:/Users/acer/Desktop/Web%20tasks/Web_Project-master/postman/F1Hub.postman_collection.json).
>>>>>>> ticket-project-update
