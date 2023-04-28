from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core import main


class Chat(APIView):
    state = -1
    FINAL_STATE = 5

    def post(self, request):
        Chat.state += 1
        if Chat.state != Chat.FINAL_STATE:
            return Response({"status": "success", "response": main.information_retrieval_module(Chat.state)},
                            status=status.HTTP_200_OK)
        return Response({"status": "success", "response": "ممنون که ما را همراهی کردید."}, status=status.HTTP_200_OK)
