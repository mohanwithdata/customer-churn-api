# Base image
FROM python:3.10-slim

# Set workdit
WORKDIR /app

# copy files

copy  . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Run API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]