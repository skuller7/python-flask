FROM python:3-alpine3.15

WORKDIR /app

COPY . /app

# RUN powershell.exe -executionPolicy unrestricted
# RUN .\Scripts\Activate.ps1
# RUN flask --app returning-data --debug run
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

# CMD python ./returning-data.py
CMD ["flask", "--app", "returning_data", "run", "--host=0.0.0.0", "--port=5000"]