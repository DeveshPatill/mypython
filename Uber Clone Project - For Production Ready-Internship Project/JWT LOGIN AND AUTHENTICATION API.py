# Write your Python code here
# Example of protected view (views.py)
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    # Return basic user profile data(Write your code here)
    user = request.user
    return Response({
        'username': user.username,
        'email': user.email,
        'is_authenticated': True
    })