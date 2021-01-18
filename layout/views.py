from django.views.generic import TemplateView
from django.shortcuts import render, redirect


# todo1: 레이아웃 완성 후 삭제
class LayoutView(TemplateView):
    template_name = 'layout/layout.html'


# drag n drop file upload snippet
def snippet_dragndrop(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        return redirect('layout:snippet_dragndrop')

    return render(request, 'layout/snippet_dragndrop.html')
