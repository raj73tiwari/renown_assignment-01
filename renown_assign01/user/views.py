from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .models import User

class UserSignUp(APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully !'}, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class GenerateOTP(APIView):
    def post(self, request):
        username = request.data.get('username')
        user = User.objects.filter(username=username).first()
        if user:
            user.generate_otp()
            return Response({'message': f'OTP is {user.otp}'}, status=status.HTTP_200_OK)
        return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

class UserLogin(APIView):
    def post(self, request):
        username = request.data.get('username')
        otp = request.data.get('otp')
        user = User.objects.filter(username=username).first()
        if user and user.is_otp_valid(otp):
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'message': 'Invalid OTP '}, status=status.HTTP_400_BAD_REQUEST)

class UpdateFullName(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        fullname = request.data.get('fullname')
        user.fullname = fullname
        user.save()
        return Response({'message': 'Fullname updated !'}, status=status.HTTP_200_OK)