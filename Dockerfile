FROM python:3-onbuild

RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader stopwords

CMD [ "python", "./webapp.py" ]