
# Capstone Corp • Python Flask Starter

A tiny Flask web app with a SQLite database to demonstrate a simple tenant portal:
- `Customers` and `Orders` tables
- HTML pages + JSON endpoints
- Health check endpoint
- Dockerfile for containerized runs

## 1) Prereqs
- Python 3.11+
- (Optional) VS Code
- Docker Desktop (for container runs)
- Git

## 2) Setup (local, no Docker)
```bash
# In project root
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# macOS/Linux
# source .venv/bin/activate

pip install -r requirements.txt
python init_db.py

# Run the app
python -m flask --app app.app run --host=0.0.0.0 --port=8080

# Open http://localhost:8080
```

## 3) Useful URLs
- `/`            → Home
- `/customers`   → HTML list + simple create form
- `/customers.json` → JSON list
- `/orders/<customerId>` → HTML list + create form
- `/health`      → JSON health

## 4) Docker (local)
```bash
docker build -t capstone-flask:dev .
docker run -p 8080:8080 capstone-flask:dev
# open http://localhost:8080
```

## 5) Notes for Azure
- This app is ready for **App Service for Containers** (Linux).
- For Azure SQL later:
  - Replace SQLite with `pyodbc` and a proper connection string.
  - Use Managed Identity with Access Tokens if you want passwordless DB access.
- Haider should provision:
  - ACR (push your image here)
  - App Service (Linux) configured to pull your image
  - VNet integration + Private Endpoint for Azure SQL (if using Azure SQL)

## 6) Git/GitHub (quickstart)
```bash
git init
git add .
git commit -m "Initial Flask starter"
# Create a new empty repo on GitHub first, then:
git remote add origin https://github.com/<your-username>/<repo-name>.git
git branch -M main
git push -u origin main
```
