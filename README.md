# Vue.js + Django Full-Stack Project

A full-stack web application with Vue.js frontend and Django REST API backend.

## Project Structure

```
├── backend/              # Django REST API
│   ├── api/              # API app with endpoints
│   ├── config/           # Django project settings
│   ├── requirements.txt  # Python dependencies
│   └── manage.py
├── frontend/             # Vue.js application
│   ├── src/
│   │   ├── components/   # Vue components
│   │   ├── views/        # Page views
│   │   ├── router/       # Vue Router configuration
│   │   ├── stores/       # Pinia state management
│   │   └── services/     # API services
│   └── package.json
└── README.md
```

## Tech Stack

### Backend
- Django 6.0
- Django REST Framework
- django-cors-headers
- SQLite (default database)

### Frontend
- Vue 3 with Composition API
- TypeScript
- Vite
- Vue Router 4
- Pinia (state management)
- Axios (HTTP client)

## Getting Started

### Prerequisites
- Python 3.12+
- Node.js 18+
- npm

### Backend Setup

1. Navigate to the backend directory:
   ```powershell
   cd backend
   ```

2. Create and activate virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```powershell
   python manage.py migrate
   ```

5. Start the Django server:
   ```powershell
   python manage.py runserver
   ```

The API will be available at `http://localhost:8000/api/`

### Frontend Setup

1. Navigate to the frontend directory:
   ```powershell
   cd frontend
   ```

2. Install dependencies:
   ```powershell
   npm install
   ```

3. Start the development server:
   ```powershell
   npm run dev
   ```

The frontend will be available at `http://localhost:5173/`

## API Endpoints

- `GET /api/health/` - Health check endpoint

## Development

### Running Both Servers

Open two terminals:

**Terminal 1 - Backend:**
```powershell
cd backend
.\venv\Scripts\Activate.ps1
python manage.py runserver
```

**Terminal 2 - Frontend:**
```powershell
cd frontend
npm run dev
```

### Environment Variables

#### Frontend (.env)
```
VITE_API_URL=http://localhost:8000/api
```

### Creating a Django Superuser

```powershell
cd backend
.\venv\Scripts\Activate.ps1
python manage.py createsuperuser
```

Access the admin panel at `http://localhost:8000/admin/`

## Building for Production

### Frontend
```powershell
cd frontend
npm run build
```

The built files will be in `frontend/dist/`

### Backend
For production, update `backend/config/settings.py`:
- Set `DEBUG = False`
- Update `ALLOWED_HOSTS`
- Configure a production database
- Set a secure `SECRET_KEY`

## License

MIT