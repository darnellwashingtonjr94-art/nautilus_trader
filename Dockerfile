# Use the official Nautilus Trader Jupyter Lab image as the base
FROM ghcr.io/nautechsystems/jupyter-lab:latest

# Set the working directory
WORKDIR /app

# Copy your requirements and node scripts
COPY requirements.txt .
COPY . /app

# Install any additional dependencies needed for your HFT node
# (e.g., web33, asyncio, or specific Monad SDKs)
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Jupyter port (and any other ports your node needs)
EXPOSE 8888

# Command to run when the container starts
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser"]
