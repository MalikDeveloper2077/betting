FROM python:3.10

WORKDIR /betmaker
COPY ./requirements.txt /betmaker/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /betmaker/requirements.txt
COPY . .

CMD ["uvicorn", "betmaker.main:app", "--host", "0.0.0.0", "--port", "8000"]
