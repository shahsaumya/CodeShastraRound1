from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from disaster.models import Person
from disaster.serializers import PersonSerializer
from django.http import Http404
from django.core import serializers

#class PeList(APIView):

#	def get(self, request):
#		tasks = Task.objects.all()
#		task_serializer = TaskSerializer(tasks, many = True)
#		return Response(task_serializer.data)


	#def post(self, request):
    #    serializer = TaskSerializer(data=request.data)
    #    if serializer.is_valid():
    #        serializer.save()
    #        return Response(serializer.data, status=status.HTTP_201_CREATED)
    #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	

 



class PersonList(APIView):

	def get_object(self, pk):
		try:
			return Snippet.objects.get(pk=pk)
		except Snippet.DoesNotExist:
			raise Http404


	#def get(self, request):
	#	teams = Team.objects.all()
	#	team_serializer = TeamSerializer(teams, many = True)
	#	return Response(team_serializer.data)

	def put(self, request, pk, format=None):
		snippet = self.get_object(pk)
		serializer = PersonSerializer(snippet, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  	

	#def post(self, request):
    #    serializer = TeamSerializer(data=request.data)
    #    if serializer.is_valid():
    #        serializer.save()
    #        return Response(serializer.data, status=status.HTTP_201_CREATED)
    #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	
	

# Create your views here.
