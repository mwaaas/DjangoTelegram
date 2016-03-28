FROM python:2.7.11-onbuild

EXPOSE 80

CMD python manage.py migrate && gunicorn --bind=0.0.0.0:80 DjangoTelegram.wsgi \
        --workers=2\
        --log-level=info \
        --log-file=-\
        --access-logfile=-\
        --error-logfile=-\
        --timeout 30\
        --reload
