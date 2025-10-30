# ✅ Base image already includes Python 3.10 + NodeJS 20
FROM nikolaik/python-nodejs:python3.10-nodejs20

# ✅ Install basic system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    curl \
    ca-certificates \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# ✅ Set working directory
WORKDIR /app

# ✅ Copy all project files
COPY . /app/

# ✅ Install Python dependencies
RUN pip3 install --no-cache-dir -U -r requirements.txt

# ✅ Fix uvloop version (PyTgCalls compatible)
RUN pip uninstall -y uvloop && pip install uvloop==0.17.0

# ✅ Make start script executable
RUN chmod +x /app/start

# ✅ Run bot
CMD ["bash", "./start"]
