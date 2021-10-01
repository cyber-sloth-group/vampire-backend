from django.contrib.auth import login, logout
from rest_framework import views, generics, response, permissions, authentication
from .serializers import LoginSerializer, UserSerializer


class CsrfExemptSessionAuthentication(authentication.SessionAuthentication):
    def enforce_csrf(self, request):
        return


class LoginView(views.APIView):
    permission_classes = (permissions.AllowAny, )
    authentication_classes = (CsrfExemptSessionAuthentication, )

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return response.Response(UserSerializer(user).data)


class LogoutView(views.APIView):

    def post(self, request):
        logout(request)
        return response.Response()


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny, )

    def perform_create(self, serializer):
        user = serializer.save()
        login(self.request, user)
        return response.Response(UserSerializer(user).data)


class UserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    lookup_field = 'pk'

    def get_object(self):
        return self.request.user
