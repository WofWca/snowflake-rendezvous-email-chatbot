FROM python:3

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

# This file is to be removed by the user after
# `python ./chatbot init ...` is run, see README.
RUN ["touch", "wait-for-init.txt"]

RUN echo 'while [ -f ./wait-for-init.txt ]; \
    do echo "wait-for-init.txt is still present. Waiting for it to get removed." \
    && sleep 5; done' \
    > wait-for-init.sh \
    && chmod +x wait-for-init.sh

CMD ./wait-for-init.sh && python ./chatbot.py serve
