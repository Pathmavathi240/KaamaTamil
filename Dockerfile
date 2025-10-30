# Base image with Python 3.10 and Node.js build tools
FROM nikolaik/python-nodejs:python3.10-nodejs20

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       curl \
       ffmpeg \
       ca-certificates \
       gnupg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install NVM and Node 18
ENV NVM_DIR=/root/.nvm
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash \
    && bash -c ". $NVM_DIR/nvm.sh \
    && nvm install 18 \
    && nvm alias default 18 \
    && nvm use default" \
    && npm install -g npm

# Ensure NVM is available in all shells
ENV PATH=$NVM_DIR/versions/node/v18.*/bin:$PATH

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app/

# Install Python dependencies
RUN pip3 install --no-cache-dir -U -r requirements.txt

# Make start script executable
RUN chmod +x /app/start

# Start the app
CMD ["/bin/bash", "-c", "./start"]
