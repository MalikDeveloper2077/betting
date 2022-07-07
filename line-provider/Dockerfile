FROM python:3.10

WORKDIR /line-provider
COPY ./requirements.txt /line-provider/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /line-provider/requirements.txt
COPY . .

CMD ["uvicorn", "line-provider.main:app", "--host", "0.0.0.0", "--port", "8080"]
