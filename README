# Using FalkorDB Langchain with Google Generative AI

## Requirements:

- Google Cloud Account and Project
- Diffbot Account and API Key
- Python
- Docker

## Setup:

### 1. Setup Google Cloud Project

- Create a new project in Google Cloud Console
- Activate the Generative Language API: [https://console.cloud.google.com/marketplace/product/google/generativelanguage.googleapis.com](https://console.cloud.google.com/marketplace/product/google/generativelanguage.googleapis.com)
- Create an API Key: [https://console.cloud.google.com/apis/credentials](https://console.cloud.google.com/apis/credentials)
- Optionally, restrict the API Key to only allow requests to the Generative Language API

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Environment Variables

```bash
export DIFFBOT_API_KEY=diffbot_api_key
export GOOGLE_API_KEY=gcp_api_key
```

### 4. Start the FalkorDB docker container

```bash
docker run -it --rm -p 6379:6379 -p 3000:3000 falkordb/falkordb
```

### 5. Run the script

```bash
python main.py
```
