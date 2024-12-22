FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

COPY *.py .

CMD ["fastapi","run","./main.py"]

# COPY main*.py ./

# RUN npm install

# COPY . .

# ENV PORT=3000

# EXPOSE 3001

# CMD [ "fastapi","run","./main.py" ]