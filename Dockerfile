# ✅ Python + NodeJS (both stable versions)
FROM python:3.10-slim

# ✅ Install system packages + NodeJS manually
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ffmpeg \
    gnupg \
    ca-certificates \
 && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
 && apt-get install -y nodejs \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# ✅ Check NodeJS installation
RUN node -v && npm -v

# ✅ Set working directory
WORKDIR /app

# ✅ Copy files
COPY . /app/

# ✅ Install Python packages
RUN pip3 install --no-cache-dir -U -r requirements.txt

# ✅ Fix uvloop version for pytgcalls
RUN pip uninstall -y uvloop && pip install uvloop==0.17.0

# ✅ Make start script executable
RUN chmod +x /app/start

# ✅ Start the bot
CMD ["bash", "./start"]
