from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from utils import user_utils

@api_view(['GET'])
def index(request, api_key):
    try:
        key = user_utils.is_authencated_by_key(api_key)
        if not key:
            raise Exception("Not valid token")
        
        return Response({"Hello" : key})
    
    except Exception as er:
        return Response(
            {"message" : er.args},
            status=status.HTTP_400_BAD_REQUEST
        )