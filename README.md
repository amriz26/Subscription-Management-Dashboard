# Subscription-Management-Dashboard

👾 The Subscription Management Dashboard is a full-stack application designed to help users track and manage their recurring subscription services (like Netflix and Spotify). It provides cost analysis, renewal reminders, and a comparison tool to help users save money by switching billing cycles.

⚙️ How it works:
Backend:A Django REST Framework API handles subscription data. When a new subscription is added, it automatically calculates the renewal date based on the billing cycle (monthly or annually). The API also computes aggregate costs and provides endpoints to list, create, and cancel subscriptions.
Frontend: The dashboard displays the total monthly spend, a renewal calendar, and a detailed cost breakdown with bar charts. Subscriptions renewing within the next 7 days are highlighted to alert the user, and a cost comparison tool estimates annual savings when switching from monthly to annual billing.

💻 Technologies Used:
Backend: Python, Django, Django REST Framework
Frontend: JavaScript (React / Vue.js)
Database: SQLite/PostgreSQL
Visualization: Charting libraries (e.g., Chart.js)

🚀 Bonus Features:
Price history: Tracks changes in subscprtion prices over time
Dark mode: Allows users to change between light and dark themes for a better experience (my favorite is dark mode!)

How to run:
### Prerequisites
- Python 3.9+
- Node.js 16+
- PostgreSQL (or SQLite for development)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/amriz26/Subscription-Management-Dashboard.git
   cd Subscription-Management-Dashboard

Backend setup:
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run the Django server
python manage.py runserver


