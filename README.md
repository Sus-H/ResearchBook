# ResearchBook

En crawler-baserad grafmotor som bygger upp ett socialt nätverk över forskare världen över, inklusive publikationer, anställningar och mjuka relationer.

## Funktioner

- Hämtar data från Semantic Scholar API
- Bygger co-author-graf
- Identifierar mjuka kopplingar
- Genererar intelligence briefs

## Användning

```bash
# Python-venv
python3 -m venv researchbook
source researchbook/bin/activate
pip install -r requirements.txt
python main.py

# Docker
docker-compose up --build
```
