from typing import Any
from django.db.models.query import QuerySet
from django.http import Http404
from django.shortcuts import render
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, ListView, DetailView

from .models import Notes
from .forms import NotesForm

class NotesDeleteView(DeleteView):
	model = Notes
	success_url = '/smart/notes'
	template_name = 'notes/notes_delete.html'

class NotesUpdateView(UpdateView):
	model = Notes
	success_url = '/smart/notes'
	form_class = NotesForm

class NotesCreateView(CreateView):
	model = Notes
	success_url = '/smart/notes'
	form_class = NotesForm

class NotesListView(LoginRequiredMixin, ListView):
	model = Notes
	context_object_name = 'notes'
	template_name = 'notes/notes_list.html'
	"""
	Login URL means that if a user is not logged in when they try using the list view,
	they will be redirected to this URL instead of seeing a 404
	"""
	login_url = "/admin"

	"""Override get_queryset to only show notes that belong to the current user"""
	def get_queryset(self):
		return self.request.user.notes.all()
	
class NotesDetailView(DetailView):
	model = Notes
	context_object_name = 'note'

def detail(request, pk):
	try:
		note = Notes.objects.get(pk=pk)
		return render(request, 'notes/notes_detail.html', {'note': note})
	except Notes.DoesNotExist:
		raise Http404('Note does not exist')