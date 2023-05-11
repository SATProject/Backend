from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json

from core import main

class Chat(APIView):
    state = "GREETING"
    FINAL_STATE = "END2"
    suggested_protocol_pool = []

    def post(self, request):
        message = json.loads(request.body.decode('utf-8'))["message"]
        res, Chat.state, Chat.suggested_protocol_pool = main.information_retrieval_module(Chat.state, message, Chat.suggested_protocol_pool)
        if Chat.state != Chat.FINAL_STATE:
            return Response({"status": "success", "response": res},
                            status=status.HTTP_200_OK)
        return Response({"status": "success", "response":  "امیدوارم تونسته باشم کمکت کنم."}, status=status.HTTP_200_OK)
