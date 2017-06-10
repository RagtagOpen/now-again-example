FROM python:2.7
RUN pip install -U python-dotenv
COPY . /app
WORKDIR /app
ENTRYPOINT ["python"]
CMD ["task.py"]
