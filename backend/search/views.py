from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from . serializers import RaceListSerializer
from . models import Race
from knox.auth import TokenAuthentication
from elasticsearch import Elasticsearch
import json

class RaceListView(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = RaceListSerializer
    pagination_class=None

    def get_queryset(self):
        races = Race.objects.all()
        return Response(races)

class RaceDetailView (APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        try:
            es = Elasticsearch([{"host": "localhost", "port": 9200, "scheme": "http"}])
            res = es.get(index="races_en", id=pk)
        except:
            return Response({"Forbidden": "Unknown ID"}, status=status.HTTP_403_FORBIDDEN)
        return Response(res['_source'])
