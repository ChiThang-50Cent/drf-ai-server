from django.contrib.auth.hashers import make_password, check_password
from users.models import User, API_Key
from uuid import UUID

def compare_password(input_password: str, hashed_password: str) -> bool:
    return check_password(input_password, hashed_password)

def check_user_exists(email: str) -> User:
    users = User.objects.filter(email__exact=email)
    if not users.exists():
        return None
    
    return users.get(email=email)

def check_user_valid(email: str, password: str) -> bool:
    user = check_user_exists(email)

    if not user:
        return False, user
    
    return check_password(password, user.password), user
    
def get_api_key(email: str) -> UUID:
    user = User.objects.get(email=email)
    return user.api_key.key

def search_api_key(api_key: str) -> bool:
    key = API_Key.objects.filter(key__exact=UUID(api_key))
    
    if not key.exists():
        return None
    
    return key.get(key=UUID(api_key))