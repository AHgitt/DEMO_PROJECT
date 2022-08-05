FROM python:3.9
WORKDIR /my-website-tracker
COPY app /my-website-tracker/app
COPY requirements.txt app.py /my-website-tracker/
RUN pip install -r requirements.txt
EXPOSE 80
EXPOSE 3306
EXPOSE 3309
EXPOSE 5000
EXPOSE 5002
CMD ["python", "./app.py"]