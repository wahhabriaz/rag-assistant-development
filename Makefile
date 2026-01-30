
### 4) `Makefile` 
```makefile
.PHONY: api ui test

api:
	uvicorn app.main:app --reload --port 8000

ui:
	streamlit run ui/streamlit_app.py

test:
	pytest -q
