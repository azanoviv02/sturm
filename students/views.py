from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import redirect
from django.views import generic

from students.models import Student


class IndexView(generic.ListView):
    template_name = 'students/index.html'
    context_object_name = 'student_list'

    def get_queryset(self):
        """Return the last five published books."""
        return Student.objects.all()


class DetailView(generic.DetailView):
    model = Student
    template_name = 'students/detail.html'

class MyProfileView(generic.DetailView):
    model = Student
    template_name = 'students/detail.html'

    def get(self, request, *args, **kwargs):
        if hasattr(self.request.user, 'student'):
            self.object = self.request.user.student
        else:
            return redirect("admin:index")
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
