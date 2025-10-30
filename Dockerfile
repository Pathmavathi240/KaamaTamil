# ✅ Base image: Python + NodeJS support
FROM python:3.11-slim

# ✅ Install system dependencies & NodeJS 20.x + git
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ffmpeg \
    gnupg \
    ca-certificates \
    bash \
    git \
 && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
 && apt-get install -y nodejs \
 && npm install -g npm@latest \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# ✅ Check NodeJS & npm versions
RUN echo "NodeJS Version:" && node -v && echo "NPM Version:" && npm -v

# ✅ Set working directory
WORKDIR /app

# ✅ Copy all files
COPY . /app/

# ✅ Install Python dependencies
RUN pip3 install --no-cache-dir -U -r requirements.txt

# ✅ Fix uvloop version (for pytgcalls)
RUN pip uninstall -y uvloop || true && pip install uvloop==0.17.0

# ✅ Give permission for start script
RUN chmod +x /app/start

# ✅ Start bot
CMD ["bash", "./start"]
