from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from projects.models import Project


class IndexView(generic.ListView):
    template_name = 'projects/index.html'
    context_object_name = 'project_list'

    def get_queryset(self):
        """Return the last five published books."""
        return Project.objects.all()


class DetailView(generic.DetailView):
    model = Project
    template_name = 'projects/detail.html'

# Create your views here.
