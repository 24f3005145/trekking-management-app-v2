# Trekking Management Application V2

A full-stack web application developed as part of the **Modern Application Development II (MAD-II)** course project.

Adventure organizations require efficient systems to manage trekking activities involving trek organizers, staff, and participants. Currently, many trekking groups rely on spreadsheets, calls, or manual coordination, which makes it difficult to manage trek approvals, participant registrations, slot availability, and booking tracking.

The application helps adventure organizations manage trekking activities, including trek creation, staff management, participant registrations, bookings, reports, and analytics.

## Tech Stack

### Backend

* Flask
* Flask REST APIs
* SQLAlchemy ORM
* SQLite
* Redis
* Celery

### Frontend

* Vue.js
* Bootstrap

## Features

### Authentication & Authorization

* Role-based access control (Admin, Trek Staff, Trekker)
* User registration and login
* Admin and Staff login management
* Secure authentication using session/JWT

### Admin Features

* Dashboard with system statistics
* Create, update, and delete treks
* Add and manage trek staff
* Assign staff to treks
* Manage users and bookings
* Search users, staff, and treks
* View reports and analytics
* Deactivate or blacklist users and staff

### Trek Staff Features

* View assigned treks
* Manage trek slots and status
* View registered participants
* Update trek progress and completion status

### Trekker Features

* Register and manage profile
* Browse and search available treks
* Book treks
* Track booking status
* View trekking history

### Background Jobs

* Daily reminders for upcoming treks
* Monthly activity reports
* Export booking history as CSV

### Performance Optimization

* Redis caching for frequently accessed data
* Optimized API responses

## Project Structure

```text
trekking-management-app-v2/
│
├── backend/
├── frontend/
├── docs/
├── README.md
└── .gitignore
```

## Database

* SQLite database created programmatically using SQLAlchemy models.
* No manual database creation.

## Future Enhancements

* Responsive UI/PWA support
* Analytics and charts
* Payment simulation
* Notifications and alerts

## Course

**Modern Application Development II (MAD-II)**
Indian Institute of Technology Madras – BS Degree Program
