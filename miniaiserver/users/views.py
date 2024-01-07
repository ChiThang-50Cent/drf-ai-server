from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer, UserLoginSerializer

from utils import user_utils

@api_view(['POST'])
def create_user(request):

    try: 
        user_serializer = UserSerializer(data=request.data)
        
        if user_serializer.is_valid():
            
            user_serializer.save()
            return Response(
                {"api-key" : user_utils\
                            .get_api_key(user_serializer\
                                         .data['email'])}
            )
        else:
            raise Exception("Data is missing")
        
    except Exception as er:
        return Response(
            {"message" : er.args},
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['POST'])
def log_in(request):

    try:
        user_login = UserLoginSerializer(data=request.data)

        if user_login.is_valid():

            is_valid_user, user = user_utils.check_user_valid(
                email=user_login.validated_data['email'],
                password=user_login.validated_data['password']
            )

            if is_valid_user:
                return Response(
                    {"api-key" : user.api_key.key},
                    status=status.HTTP_200_OK)
            else:
                raise Exception("Wrong email or password")
        else:
            raise Exception("Something went wrong")
    
    except Exception as er:
        return Response(
            {"message" : er.args},
            status=status.HTTP_400_BAD_REQUEST
        )

