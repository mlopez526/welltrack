# 🐳 Docker Deployment Guide

## Quick Start with Docker

### Option 1: Using Docker Compose (Recommended)

```bash
# Build and start the container
docker-compose up --build

# Access the app at: http://localhost:5000
```

### Option 2: Using Docker CLI

```bash
# Build the image
docker build -t welltrack:latest .

# Run the container
docker run -p 5000:5000 welltrack:latest

# Access the app at: http://localhost:5000
```

---

## What's Included

The Docker container includes:
- ✅ Python 3.11 runtime
- ✅ Flask backend with all dependencies
- ✅ Frontend HTML served at root (`/`)
- ✅ All API endpoints at `/api/*`
- ✅ SQLite database (auto-created)

---

## Docker Commands

### Build Image
```bash
docker build -t welltrack:latest .
```

### Run Container
```bash
# Basic run
docker run -p 5000:5000 welltrack:latest

# Run in background (detached)
docker run -d -p 5000:5000 --name welltrack-app welltrack:latest

# Run with persistent data volume
docker run -p 5000:5000 -v $(pwd)/data:/data -e DB_NAME=/data/welltrack.db welltrack:latest
```

### Manage Container
```bash
# View running containers
docker ps

# Stop container
docker stop welltrack-app

# Start container
docker start welltrack-app

# View logs
docker logs welltrack-app

# Remove container
docker rm welltrack-app
```

### Clean Up
```bash
# Remove image
docker rmi welltrack:latest

# Remove all stopped containers
docker container prune

# Remove unused images
docker image prune
```

---

## Using Docker Compose

### Start Services
```bash
# Build and start in foreground
docker-compose up --build

# Start in background
docker-compose up -d --build
```

### Manage Services
```bash
# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Restart services
docker-compose restart

# View running services
docker-compose ps
```

---

## Access the Application

Once the container is running:

**Frontend:** `http://localhost:5000`  
**API Endpoints:**
- `POST http://localhost:5000/api/register`
- `POST http://localhost:5000/api/login`
- `POST http://localhost:5000/api/mood`
- `GET http://localhost:5000/api/mood/history`
- `POST http://localhost:5000/api/journal`
- `GET http://localhost:5000/api/journal/history`

---

## Data Persistence

### Option 1: Named Volume
```bash
docker run -p 5000:5000 -v welltrack-data:/app welltrack:latest
```

### Option 2: Bind Mount
```bash
docker run -p 5000:5000 -v $(pwd)/data:/app/data welltrack:latest
```

The SQLite database (`welltrack.db`) will persist in the volume.

---

## Environment Variables

```bash
# Set Flask environment
docker run -p 5000:5000 -e FLASK_ENV=production welltrack:latest

# Custom port (requires app.py modification)
docker run -p 8080:5000 welltrack:latest
```

---

## Troubleshooting

### Port Already in Use
```bash
# Use different host port
docker run -p 8080:5000 welltrack:latest
# Access at: http://localhost:8080
```

### Container Won't Start
```bash
# Check logs
docker logs welltrack-app

# Run interactively
docker run -it welltrack:latest /bin/bash
```

### Database Issues
```bash
# Remove volume and restart
docker-compose down -v
docker-compose up --build
```

---

## Production Deployment

For production, consider:

1. **Use Gunicorn instead of Flask dev server:**
```dockerfile
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

2. **Add health check:**
```dockerfile
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:5000/api/debug/db || exit 1
```

3. **Use environment variables for secrets**

4. **Deploy to cloud:**
   - AWS ECS/Fargate
   - Google Cloud Run
   - Azure Container Instances
   - Heroku

---

### Using Production Docker Compose File
```bash
docker-compose -f production-compose.yml up --build
```


## Testing the Dockerized App

```bash
# Start container
docker-compose up -d

# Wait a few seconds for startup
sleep 3

# Test API
curl http://localhost:5000/api/debug/db

# Open in browser
open http://localhost:5000  # Mac
start http://localhost:5000  # Windows
xdg-open http://localhost:5000  # Linux
```

---

## File Structure

```
welltrack/
├── Dockerfile              # Container definition
├── docker-compose.yml      # Compose configuration
├── .dockerignore          # Files to exclude
├── backend/
│   ├── app.py             # Flask app (serves frontend too)
│   └── requirements.txt   # Python dependencies
└── frontend/
    └── index.html         # Web interface
    └── newindex.html      # Web interface
```

---

## Quick Reference

| Command | Description |
|---------|-------------|
| `docker-compose up --build` | Build and start |
| `docker-compose down` | Stop and remove |
| `docker-compose logs -f` | View logs |
| `docker ps` | List containers |
| `docker logs <container>` | View container logs |

---

**Your WellTrack app is now containerized and ready to deploy anywhere!** 🚀
