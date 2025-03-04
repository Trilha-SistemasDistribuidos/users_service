from rest_framework import viewsets, status
from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save()
    
    # get /api/user/usuarios/ returns only the user that is logged in
    def get_queryset(self):
        return Usuario.objects.filter(id=self.request.user.id)
    
    # patch /api/user/usuarios/{id}/ 
    def partial_update(self, request, **kwargs):
        id = kwargs.get('pk')
        user = Usuario.objects.get(id=id)
        if user.id != request.user.id or not user.check_password(request.data.get('password')):
            return Response({'detail': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)        
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        if 'password' in serializer.validated_data:
            serializer.validated_data.pop('password')
            serializer.validated_data.pop('password2')
        serializer.save()
        return Response(serializer.data)
    
class UsuarioCreateListView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]  # Adicione autenticação

class GuideViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.filter(tipo='Guia')
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]