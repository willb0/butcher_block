FROM python:3.8-slim

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/requirements.txt

RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt

COPY src/ /usr/src/app/src/


EXPOSE 8501

CMD ["streamlit","run","src/dash.py"]






