from django.views.generic import TemplateView, ListView, DeleteView
from django.views.generic.edit import FormView, UpdateView, CreateView
from django.shortcuts import render, redirect

from .forms import UserCreateForm, UserUpdateForm
from .models import User


class UserList(ListView):
    template_name = 'users/user_list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']

        page_numbers_range = 5
        max_index = len(paginator.page_range)

        current_page = int(self.request.GET.get('page', 1))

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range
        context['last_page'] = max_index
        return context


class UserDetail(DeleteView):
    template_name = 'users/user_detail.html'

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset


class UserCreate(CreateView):
    template_name = 'users/user_create.html'
    form_class = UserCreateForm
    model = User

    def get_success_url(self):
        return f'/users/user-detail/{self.object.pk}/'


class UserUpdate(UpdateView):
    template_name = 'users/user_update.html'
    form_class = UserUpdateForm
    model = User

    def get_success_url(self):
        if self.object.status:
            return f'/users/user-detail/{self.object.pk}/'
        else:
            return '/users/user-list/'
