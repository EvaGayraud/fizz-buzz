FROM python:3.12.8-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose port
EXPOSE 8000

CMD ["uvicorn", "fizz_buzz.__main__:app", "--host", "0.0.0.0", "--port", "8000"]
