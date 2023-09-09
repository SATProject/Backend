from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from sentence_transformers import SentenceTransformer
import joblib
from core import speech2text
from core import text2speech
from core import main
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from urllib.parse import unquote


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
    model = SentenceTransformer("HooshvareLab/bert-base-parsbert-uncased")
    protocol = ""
    last_state = "GREETING"
    users_state = {}

    def post(self, request):
        decoded_text = unquote(request.body)
        print("boddyyyyyy", decoded_text)

        if "message" not in decoded_text:
            username = decoded_text[9:].replace("+", " ")
            Chat.users_state[username] = "GREETING"
            return Response({"status": "success"})

        # message = request.body.decode('utf-8')[8:] #json.loads(request.body.decode('utf-8'))["message"]
        username = decoded_text.split("&")[0][9:].replace("+", " ")
        message = decoded_text.split("&")[1][8:].replace("+", " ")
        # print(message.decode("utf-8"))
        print("text", message)
        try:
            file_obj = request.FILES["voice"]
            path = default_storage.save("stt/voice.wav", ContentFile(file_obj.read()))
            message = speech2text.speech2text("stt/voice.wav")
            print("voice", message)
        except:
            print("file not found!")

        if message == "restart":
            Chat.users_state[username] = "GREETING"

        # ## USAGE: DAILY DIARY
        # Chat.last_state = Chat.state
        # ###

        (
            res,
            Chat.users_state[username],
            Chat.suggested_protocol_pool,
            Chat.buttons,
            Chat.additionals,
            Chat.addtional_num,
            Chat.name,
            Chat.dof,
            Chat.previous_questions_embeddings,
        ) = main.information_retrieval_module(
            Chat.users_state[username],
            message,
            Chat.suggested_protocol_pool,
            Chat.additionals,
            Chat.addtional_num,
            Chat.name,
            Chat.dof,
            Chat.previous_questions_embeddings,
            Chat.model,
        )

        ## DAILY DIARY
        # if res == "لطفا تمرین زیر رو انجام بده.":
        #     Chat.protocol = res.title
        # if Chat.last_state == "PROTOCOL_SUGGESTING3":
        #     with open("../core/daily_diary.txt", "a") as f:
        #         f.write("protocol:", Chat.protocol, "message:", message)
        ###

        if Chat.users_state[username] != Chat.FINAL_STATE:
            if res is str:
                text2speech.text2speech(res)
                print("speech created!")
            print(res)
            return Response(
                {"status": "success", "response": res, "buttons": Chat.buttons},
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "status": "end",
                "response": "امیدوارم تونسته باشم کمکت کنم.",
                "buttons": Chat.buttons,
            },
            status=status.HTTP_200_OK,
        )
