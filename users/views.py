from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, View
from django.views.generic.edit import FormView, UpdateView, CreateView
from django.db.models import Q

from .forms import UserCreateForm, UserUpdateForm
from .models import User


class UserList(LoginRequiredMixin, ListView):
    template_name = 'users/user_list.html'
    paginate_by = 2

    def get_queryset(self):
        queryset = User.objects.filter(status=True)
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(username__icontains=q) |
                Q(name__icontains=q) |
                Q(department__name__icontains=q) |
                Q(position__name__icontains=q) |
                Q(phone__icontains=q) |
                Q(email__icontains=q)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # pagination
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


class UserDetail(LoginRequiredMixin, DeleteView):
    template_name = 'users/user_detail.html'

    def get_queryset(self):
        queryset = User.objects.filter(status=True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['change_password_url'] = reverse_lazy('users:change_password',
                                                      kwargs={'pk': self.object.pk})
        return context


class UserCreate(LoginRequiredMixin, CreateView):
    template_name = 'users/user_create.html'
    form_class = UserCreateForm
    model = User

    def get_success_url(self):
        return f'/users/user-detail/{self.object.pk}/'


class UserUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'users/user_update.html'
    form_class = UserUpdateForm
    model = User

    def get_success_url(self):
        if self.object.status:
            return f'/users/user-detail/{self.object.pk}/'
        else:
            return '/users/user-list/'


class UserDelete(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        user = User.objects.get(pk=self.kwargs['pk'])
        user.status = False
        user.save()
        return redirect('users:user_list')


class PasswordUpdate(LoginRequiredMixin, FormView):
    template_name = 'users/admin_password_change_form.html'
    form_class = SetPasswordForm

    def get_success_url(self):
        return '/users/user-list/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = User.objects.get(pk=self.kwargs['pk'])
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class MyProfile(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        context = {
            'object': request.user,
            'change_password_url': reverse_lazy('password_change')
        }
        return render(request, 'users/user_detail.html', context)
