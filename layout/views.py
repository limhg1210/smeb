from django.views.generic import TemplateView


# todo1: 레이아웃 완성 후 삭제
class LayoutView(TemplateView):
    template_name = 'layout/layout.html'
