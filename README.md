# Subscription-Management-Dashboard
A full-stack application to track and manage subscription services (like Netflix, Spotify, etc.). The system helps users monitor subscription costs, get renewal reminders, view spending breakdowns, and compare billing options to potentially save money.

Overview

The Subscription Management Dashboard is designed to give users complete visibility over their recurring subscription expenses. It features a Django REST Framework (DRF) backend and a modern front-end dashboard that provides:

➪Automatic renewal date calculations based on billing cycles.
➪A detailed cost analysis (both monthly and annually) using Django annotations.
➪A visual dashboard to track spending, view renewal calendars, and see cost breakdowns by service.
➪Alerts for upcoming renewals, helping avoid service interruptions.

Features
Core Features
➪Backend API (Django/DRF):
  ➪Models: Data models to store subscription details including service name, pricing, billing cycle, and renewal dates.
  ➪API Endpoints:
    ➪GET /api/subscriptions/ – Lists all subscriptions with computed annual and monthly costs.
    ➪POST /api/subscriptions/ – Creates a new subscription. Automatically calculates the renewal_date based on the selected billing cycle.
    ➪DELETE /api/subscriptions/{id}/ – Cancels a subscription by ID.
  ➪Cost Aggregation: Uses Django annotations to compute aggregate costs.
➪Frontend Dashboard:
  ➪Overview: Displays total monthly spend and a renewal calendar.
  ➪Visualization: Presents cost breakdowns per service using bar charts.
  ➪Alerts: Highlights subscriptions that are due to renew within the next 7 days.
  ➪Comparison Tool: Provides an estimate of annual savings if switching from monthly to annual billing.

Bonus Features
➪Price History: Track historical changes in subscription prices.
➪Dark Mode: Toggle between light and dark themes for improved user experience.

Technologies Used
➪Backend: Python, Django, Django REST Framework
➪Frontend: JavaScript (and optionally a framework like React or Vue.js)
➪Database: SQLite/PostgreSQL (configurable)
➪Visualization: Charting libraries for rendering cost breakdowns (e.g., Chart.js, D3.js)
