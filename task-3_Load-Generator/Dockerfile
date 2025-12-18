FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy our Python script into the image
COPY loadgen.py .

# Install required Python packages
RUN pip install --no-cache-dir requests

# Default environment variables (can be overridden)
# For Kubernetes use, this will hit the Service inside the cluster
ENV TARGET=http://javabenchmark-service.default.svc.cluster.local:8080/primecheck
ENV FREQUENCY=2

# Run the load generator
CMD ["python", "loadgen.py"]

