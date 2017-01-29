from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from disaster.models import Person,HelpGiver,IndividualDetails,GroupDetails
from disaster.serializers import PersonSerializer
from django.http import Http404
from django.core import serializers
from pushy import PushyAPI

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

def help(request):
 	details = requests.get(url)
 	GroupDetails.objects.create(data_token=details[token],number=details[number],lat=details[lat],lon=details[lon])
 	obj = GroupDetails.objects.get(data_token=details[token])
 	for user in details[users]:
            IndividualDetails.objects.create(name=user['name'],age=user['age'],gender=user['gender'],key=obj.id)
	return render(request,'.html')

def search(request):
	seekerList=GroupDetails.objects.order_by("id")
	giverList=HelpGiver.details.order_by("id")
	distance_min=0
	for group in seekerList:
		fly=None
		for family in giverList:
			if family[capacity]>=group[number]:
				json = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=19.0815, 72.8377&destinations=19.1155, 72.8727&key=AIzaSyCvCg-Ed0uayEUcNWIgVb_6pRV8imB5kEM")
				distance=json[rows][elements][distance][value]
				if (distance<distance_min):
					fly=family

		if fly!=None:		
			fly.capacity=fly.capacity-group	
      		data = {'name': fly.name,'address':fly.address,'lat':fly.lat,'lon':fly.lon}
        	PushyAPI.sendPushNotification(data, group.data_token)





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
def packages(request):
        return render(request, 'index.html')

def animate(request):
        return render(request, 'animate.html')

def index(request):
        return render(request, 'index.html')

def disaster(request):
        return render(request, 'template-alerts.html')

def about(request):
        return render(request, 'about.html')

def register(request):
        return render(request, 'customer-register.html')
