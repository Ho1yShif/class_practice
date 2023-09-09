from django.http import Http404
from django.shortcuts import render
from django.views.generic.edit import DeleteView
from django.views.generic import CreateView, UpdateView, ListView, DetailView

from .models import Notes
from .forms import NotesForm

class NotesDeleteView(DeleteView):
	model = Notes
	success_url = '/smart/notes'

class NotesUpdateView(UpdateView):
	model = Notes
	success_url = '/smart/notes'
	form_class = NotesForm

class NotesCreateView(CreateView):
	model = Notes
	success_url = '/smart/notes'
	form_class = NotesForm

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