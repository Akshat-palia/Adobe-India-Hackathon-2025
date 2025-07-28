FROM --platform=linux/amd64 python:3.10-slim

# Set working directory
WORKDIR /app

# Install required library
RUN pip install --no-cache-dir pymupdf

# Copy processing script
COPY process_pdfs.py .

# Run the script when the container starts
CMD ["python", "process_pdfs.py"]
