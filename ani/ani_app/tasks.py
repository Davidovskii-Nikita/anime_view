from time import sleep

from ani.celery import app as celery_app
import logging

@celery_app.task
def send_mail(mail: str):
    sleep(5)
    logging.info(f'message to {mail} done')

