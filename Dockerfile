FROM ubuntu
FROM python:3.7.5-slim
RUN apt update
COPY Project.py .
CMD ["python", "Project.py"]
