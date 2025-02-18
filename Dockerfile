FROM python:3.9

WORKDIR /app

COPY app.py train_model.py requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

RUN python train_model.py

EXPOSE 5000

CMD ['python', 'app.py']