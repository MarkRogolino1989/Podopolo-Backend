from .models import Notes
from .serializer import noteSerializers
from rest_framework import generics
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import viewsets

class NotesList(generics.ListCreateAPIView):
    queryset = Notes.objects.all()
    serializer_class = noteSerializers

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class NotesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notes.objects.all()
    serializer_class = noteSerializers

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

def fnShareNotes(request, pk):
    if request.method == "POST":
        share_id = request.POST['share_id']
        item = Notes.objects.get(id=pk)
        notes_name = item.notes_name
        share_item = noteSerializers(data={"notes_id":share_id, "notes_name":notes_name})
        if share_item.is_valid():
            share_item.save()
            return JsonResponse({"State": "Success Share the note"})
        return JsonResponse({"State": "Request data is not correct"})

    return JsonResponse({"State": "Bad Request"})



class YourModelViewSet(viewsets.ModelViewSet):
    serializer_class = noteSerializers

    def get_queryset(self):
        queryset = Notes.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        keyword = self.request.query_params.get('q', None)
        if keyword is not None:
            queryset = queryset.filter(name__icontains=keyword)

        serializer = noteSerializers(queryset, many=True)
        return Response(serializer.data)

def fnSearchNote(request):
    if request.method == "GET":
        query = request.GET['q']
        print(query)
        queryset = Notes.objects.all()
        if query is not None:
            queryset = queryset.filter(notes_name__icontains=query)
        serializer = noteSerializers(queryset, many=True)
        return JsonResponse({"data": serializer.data})
    return JsonResponse({"State": "Bad Request"})

