from django.shortcuts import render
from django.http import Http404
from .models import Notes
from django.views.generic import CreateView, ListView, DetailView

class NotesCreateView(CreateView):
	model = Notes
	fields = ['title', 'text']
	"""Modified this to redirect to the notes list page after creating a new note via the form"""
	success_url = '../notes'

class NotesListView(ListView):
	model = Notes
	context_object_name = 'notes'
	template_name = 'notes/notes_list.html'

class NotesDetailView(DetailView):
	model = Notes
	context_object_name = 'note'

def detail(request, pk):
	try:
		note = Notes.objects.get(pk=pk)
		return render(request, 'notes/notes_detail.html', {'note': note})
	except Notes.DoesNotExist:
		raise Http404('Note does not exist')
