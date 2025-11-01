# PyWebApp - Modern Python Web Application

A high-performance, beautiful web application built with Python, FastAPI, and Tailwind CSS.

## Features

- ⚡ **Fast Performance** - Built with FastAPI for lightning-fast response times
- 🎨 **Modern Design** - Beautiful, responsive UI with Tailwind CSS
- 🔌 **RESTful API** - Complete CRUD operations with automatic OpenAPI documentation
- 📊 **Dashboard** - Interactive dashboard with statistics and task management
- 🚀 **Static Generation** - Pre-render pages for optimal performance

## Technology Stack

### Backend
- **FastAPI** - Modern, fast web framework for building APIs
- **Pydantic** - Data validation using Python type annotations
- **Uvicorn** - Lightning-fast ASGI server
- **Jinja2** - Powerful template engine

### Frontend
- **Tailwind CSS** - Utility-first CSS framework
- **Responsive Design** - Works on all devices
- **Modern Animations** - Smooth transitions and effects

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Option 1: Run as Dynamic Web Server

Start the FastAPI development server:
```bash
python -m uvicorn app.main:app --reload
```

Then open your browser to:
- Home: http://localhost:8000
- About: http://localhost:8000/about
- API Docs: http://localhost:8000/docs
- Alternative API Docs: http://localhost:8000/redoc

### Option 2: Generate Static Files

Generate static HTML files for deployment:
```bash
python generate_static.py
```

Static files will be created in `static/generated/` directory. You can:
- Open them directly in a browser
- Serve with any static file server
- Deploy to static hosting platforms (Netlify, Vercel, GitHub Pages, etc.)

## API Endpoints

- `GET /api/tasks` - Get all tasks
- `GET /api/tasks/{id}` - Get task by ID
- `POST /api/tasks` - Create new task
- `PUT /api/tasks/{id}` - Update task
- `DELETE /api/tasks/{id}` - Delete task
- `GET /api/stats` - Get statistics

## Project Structure

```
/vercel/sandbox/
├── app/
│   ├── __init__.py
│   └── main.py              # FastAPI application
├── templates/
│   ├── base.html            # Base template
│   ├── index.html           # Home page
│   └── about.html           # About page
├── static/
│   └── generated/           # Generated static files
├── generate_static.py       # Static site generator
├── requirements.txt         # Python dependencies
└── README_PROJECT.md        # This file
```

## Development

The application uses:
- **FastAPI** for routing and API endpoints
- **Jinja2** for HTML templating
- **Pydantic** for data validation
- **In-memory storage** for demo purposes (can be replaced with a database)

## Deployment

### Static Deployment
1. Generate static files: `python generate_static.py`
2. Deploy the `static/generated/` directory to any static host

### Dynamic Deployment
1. Deploy the entire application to a Python hosting platform
2. Set the start command to: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

## Created By

**Amiya** - A modern Python web application showcasing best practices in web development.

## License

MIT License - Feel free to use this project for learning and development!
