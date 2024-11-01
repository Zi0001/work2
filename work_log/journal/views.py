from django.shortcuts import render
from django.views.generic import CreateView
from django.core.paginator import Paginator

from .models import Journal
from .forms import JournalForm

from django.conf import settings


def test(request):
    jornal = Journal.objects.all()
    # context = {'jornal': jornal}
    paginator = Paginator(jornal, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj':page_obj}

    return render(request, 'journal/index.html', context )


class JournalCreate(CreateView):
    model = Journal
    form_class = JournalForm
    template_name = 'journal/create.html'

