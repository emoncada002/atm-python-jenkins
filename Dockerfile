FROM app-python-base:latest
COPY . /app
CMD ["python", "main.py"]
