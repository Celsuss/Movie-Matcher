FROM python:3.9

WORKDIR /app
COPY . .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000

# ENTRYPOINT ["python"]
# CMD ["app.py"]
# CMD [ "flask --app api run" ] 

# ENTRYPOINT ["flask"]
# CMD ["run"]