from django.shortcuts import render
from rest_framework.views import APIView
from structlog import get_logger
from rest_framework.response import Response
from rest_framework import status


class TelegramBotView(APIView):

    def post(self, req):
        logger = get_logger(__name__)

        logger.info('start', data=req.data)

        return Response(status=status.HTTP_200_OK)
