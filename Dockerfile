FROM python:3.10-slim

WORKDIR /ruka

COPY requirements.txt .

# Install dotenv explicitly first
RUN pip install --no-cache-dir python-dotenv

# Then install other requirements
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "-m", "RUKA"]
