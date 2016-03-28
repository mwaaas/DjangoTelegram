from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.conf import settings
import telepot
import os


class Command(BaseCommand):
    """
    Command to set up telegram webhook
    """

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument('--telgram_url',
            dest='telgram_url',
            default='https://www.tumacredo.com/telegram/',
            help=('telegram url'))

        default_cert = os.path.join(settings.BASE_DIR, 'YOURPUBLIC.pem')

        parser.add_argument('--certificate',
            dest='cert',
            default=default_cert,
            help=('cert'))

    def handle(self, *args, **options):
        telgram_app_url = options['telgram_url']

        cert = options["cert"]

        bot = telepot.Bot(settings.TELEGRAM_TOKEN)
        cert_file = open(cert)
        results = bot.setWebhook(telgram_app_url, cert_file)

        bot.setWebhook(telgram_app_url, )
        
        print("web hook was created successfully {}".format(results))


