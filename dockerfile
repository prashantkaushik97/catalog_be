# Use an official Python runtime as a parent image.
FROM python:3.10-slim

# Prevent Python from writing .pyc files to disk.
ENV PYTHONDONTWRITEBYTECODE=1
# Prevent Python from buffering stdout and stderr.
ENV PYTHONUNBUFFERED=1

# Set a working directory for the app.
WORKDIR /app

# Install system dependencies (if needed, e.g., for psycopg2 or other C dependencies)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
 && rm -rf /var/lib/apt/lists/*

# Copy only requirements.txt first for caching purposes.
COPY requirements.txt /app/

# Upgrade pip and install Python dependencies.
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire project into the container.
COPY . /app/

# Collect static files to the directory defined by STATIC_ROOT in settings.py.
RUN python manage.py collectstatic --noinput

# Expose port 8000 to the outside world.
EXPOSE 8000

# Run Gunicorn to serve the Django app.
CMD ["gunicorn", "product_catalog.wsgi:application", "--bind", "0.0.0.0:8000"]
