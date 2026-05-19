# University Lost & Found Portal

A clean, user-friendly Django application designed for university campuses to help students report lost items and recover found belongings quickly without friction.

## 🚀 Features
* **Public Open Reporting:** Students can instantly post lost or found items with custom descriptions, images, and contact info without needing an account.
* **Backend Security Bounds:** Deletion and status alterations are restricted to the Django Administrative Dashboard to avoid unauthorized data tampering.
* **Real-Time Workspace Filter:** Features an interactive search engine on the homepage for finding specific entries seamlessly.
* **Archival Tracking:** Items successfully returned can be marked as `Claimed` in the dashboard to cleanly filter them off the public feed while preserving historical tracking logs.

## 🛠️ Technology Stack
* **Backend Framework:** Django (Python)
* **Database:** SQLite
* **Frontend Design:** HTML5, CSS3, Bootstrap 5

## 📁 Project Architecture
* `config/` - Core project settings, configuration files, and main routing.
* `lostnfound/` - Application-specific data models, dynamic views, and sub-routing components.
* `templates/` - Front-end HTML templates (`home.html`, `add_item.html`).

---
*Developed for structural database design and version management presentation criteria.*
