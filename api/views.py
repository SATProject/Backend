from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from sentence_transformers import SentenceTransformer

from core import main

class Chat(APIView):
    state = "GREETING"
    FINAL_STATE = "END2"
    buttons = []
    suggested_protocol_pool = []
    additionals = []
    addtional_num = 0
    name = ""
    dof = 0
    previous_questions_embeddings = []
    model = SentenceTransformer('HooshvareLab/bert-base-parsbert-uncased')
    protocol = ""
    last_state = "GREETING"
  
    def post(self, request):
        message = json.loads(request.body.decode('utf-8'))["message"]
        if message == "restart":
            Chat.state = "GREETING"

        ## USAGE: DAILY DIARY
        Chat.last_state = Chat.state
        ###

        res, Chat.state, Chat.suggested_protocol_pool, Chat.buttons, Chat.additionals, Chat.addtional_num, Chat.name, Chat.dof, Chat.previous_questions_embeddings = main.information_retrieval_module(Chat.state, message, Chat.suggested_protocol_pool, Chat.additionals, Chat.addtional_num, Chat.name, Chat.dof, Chat.previous_questions_embeddings, Chat.model)
        
        ## DAILY DIARY
        if res == "لطفا تمرین زیر رو انجام بده.":
            Chat.protocol = res.title
        if Chat.last_state == "PROTOCOL_SUGGESTING3":
            with open('../core/daily_diary.txt', 'a') as f:
                f.write('protocol:', Chat.protocol, 'message:', message)
        ###

        if Chat.state != Chat.FINAL_STATE:
            return Response({"status": "success", "response": res, "buttons": Chat.buttons},
                            status=status.HTTP_200_OK)
        return Response({"status": "end", "response":  "امیدوارم تونسته باشم کمکت کنم.", "buttons": Chat.buttons}, status=status.HTTP_200_OK)
