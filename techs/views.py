from operator import and_

from django.db.models import Q
from django.views import generic

from techs.models import Tech


class MainView(generic.ListView):
    template_name = 'techs/main.html'
    context_object_name = 'tech_list'

    def get_queryset(self):
        """Return the last five published books."""
        return Tech.objects.all()


class IndexView(generic.ListView):
    template_name = 'techs/index.html'
    context_object_name = 'tech_list'

    def get_criteria_list(self):
        return [~Q(pk=None)]

    def get_queryset(self):
        tech_list = Tech.objects \
            .filter(reduce(and_, self.get_criteria_list())) \
            .distinct()
        return tech_list


class CategoryIndexView(IndexView):
    def get_criteria_list(self):
        category = self.kwargs['category']

        category_criteria = Q(tags__slug=category)

        return [category_criteria]


class DetailView(generic.DetailView):
    model = Tech
    template_name = 'techs/detail.html'

# Create your views here.
