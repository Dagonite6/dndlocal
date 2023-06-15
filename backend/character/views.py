from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from . serializers import ListSerializer, CreateSerializer, CharacterSerializer
from .models import Character

#получаем список персонажей конкретного юзера, в персаж серилизруем не всю инфу а ток ту что надо для первью
class ListView(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = ListSerializer

    def get_queryset(self):
        user = self.request.user
        characters = Character.objects.filter(user=self.request.user)
        return characters

#get, put, patch and delete методы инхеретим 
class DetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = CharacterSerializer  

    #превентим возможность любого залогиненоно юзера делать операции над любыми персонажами, а не своими
    def get_queryset(self):
        return Character.objects.filter(user=self.request.user)
     
    #из ссылки тащим айди и получаем инфу по конкретному персонажу
    def retrieve(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        try:
            object = Character.objects.filter(user=self.request.user).get(pk=kwargs['pk'])
        except:
            return Response({"Forbidden": "Unknown ID"}, status=status.HTTP_403_FORBIDDEN)
        serializer = CharacterSerializer(object)
        return Response(serializer.data)
        

class CreateView(generics.CreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = CreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        character = serializer.data
        
        return Response({
            "character": character
        })
