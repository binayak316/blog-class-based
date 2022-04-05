from django.shortcuts import render
from django.views import generic
from .models import POST
# Create your views here.

class PostList(generic.ListView):
    queryset = POST.objects.filter(status=1).order_by('-created_on')

    # query set is used for create filter order delete views .py ma use hunxa queryset
    # filter status=1 ra orderby kina hunxa vane publish status vako matra blog ma dekhine ra recently created frontend ma dekhine
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = POST
    template_name = 'post_detail.html'
