# ✅ Base image: Python + NodeJS support
FROM python:3.11-slim

# ✅ Install system dependencies & NodeJS 20.x
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ffmpeg \
    gnupg \
    ca-certificates \
    bash \
 && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
 && apt-get install -y nodejs \
 && npm install -g npm@latest \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# ✅ Confirm NodeJS and npm installation
RUN echo "NodeJS Version:" && node -v && echo "NPM Version:" && npm -v

# ✅ Set working directory
WORKDIR /app

# ✅ Copy all bot files
COPY . /app/

# ✅ Install Python requirements
RUN pip3 install --no-cache-dir -U -r requirements.txt

# ✅ Fix uvloop version (for pytgcalls)
RUN pip uninstall -y uvloop || true && pip install uvloop==0.17.0

# ✅ Give permission to start script
RUN chmod +x /app/start

# ✅ Run the bot
CMD ["bash", "./start"]
