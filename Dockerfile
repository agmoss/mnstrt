FROM python:3.10-slim 
EXPOSE 5432
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "-m", "mnstrt", "-opt", "collect_schedule"]
