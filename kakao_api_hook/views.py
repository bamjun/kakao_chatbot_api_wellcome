from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


class Test_api(APIView):
    def post(self, request):
        response = {
            "version": "2.0",
            "template": {"outputs": [{"simpleText": {"text": "hi"}}]},
        }
        return Response(response)
