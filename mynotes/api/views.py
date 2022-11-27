from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Return a single note object'
        }
    ]
    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True) #many is telling the interpreter to return back multiple
    return Response(serializer.data) #since serializer comes back as an object we need to access it's associated data

@api_view(['GET'])
def getNote(request, pk):
    
    notes = Note.objects.get(id=pk)
    serializer = NoteSerializer(notes, many=False) #many is telling the interpreter to return back multiple
    return Response(serializer.data)