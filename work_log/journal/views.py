from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.core.paginator import Paginator

from .models import Journal
from .forms import JournalForm


def test(request):
    jornal = Journal.objects.all()
    # context = {'jornal': jornal}
    paginator = Paginator(jornal, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}

    return render(
        request,
        'journal/index.html',
        context
    )


class JournalCreate(CreateView):
    model = Journal
    form_class = JournalForm
    template_name = 'journal/create.html'


class Edit(UpdateView):
    model = Journal
    fields = ['place', 'executor']
    template_name = 'journal/edit.html'
    success_url = reverse_lazy('journal:test')

    def get_object(self):
            # Получаем id записи из URL
            id = self.kwargs.get('pk') 
            # Возвращаем объект Journal с соответствующим id
            return get_object_or_404(Journal, pk=id)
    # journal = Journal.objects.get(pk=pk)
    # context = {'journal':journal}
    # return render(request, 'journal/edit.html', context)
