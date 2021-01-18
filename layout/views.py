from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# todo1: 레이아웃 완성 후 삭제
class LayoutView(TemplateView):
    template_name = 'layout/layout.html'


@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    template_name = 'layout/index.html'


# drag n drop file upload snippet
def snippet_dragndrop(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        return redirect('layout:snippet_dragndrop')

    return render(request, 'layout/snippet_dragndrop.html')
