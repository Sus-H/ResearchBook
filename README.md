# ResearchBook

A tool to build a social graph of researchers worldwide using Google Scholar and Chalmers ODR data sources.

## Features
- Fetch author data from Google Scholar (via SerpAPI)
- Fetch author data from Chalmers ODR
- Build co-author social graph
- Generate a brief summary of co-author relations
- Interactive web UI with Streamlit

## Setup

### Python virtual environment

```bash
python3 -m venv researchbook
source researchbook/bin/activate
pip install -r requirements.txt
```

### Environment variables

Create a `.env` in project root:
```
SERPAPI_API_KEY=your_serpapi_key_here
CHALMERS_ODR_API_KEY=your_odr_api_key_here
```

### Run CLI

```bash
python main.py
```

### Run web UI

```bash
streamlit run app/ui.py
```

### Docker

```bash
docker-compose up --build
```
