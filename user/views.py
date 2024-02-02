from django.contrib import messages
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, ListView, DeleteView
from django.utils.translation import gettext_lazy as _
from user.forms import UserCreationForm

from user.models import Registration

User = get_user_model()


class UserCreateView(CreateView):

    model = Registration
    form_class = UserCreationForm
    template_name = 'user_create.html'
    success_url = reverse_lazy('user:user_views')

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _("user successfully Created")
        )
        return super().form_valid(form)


class UserUpdateView(UpdateView):

    model = Registration
    form_class = UserCreationForm
    template_name = 'user_update.html'
    success_url = reverse_lazy('user:user_views')

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _("user successfully Updated")
        )
        return super().form_valid(form)


class UserListView(ListView):

    model = Registration
    template_name = 'user_view.html'
    context_object_name = 'users'
    paginate_by = 8


class UserDeleteView(DeleteView):
    model = Registration
    template_name = 'user_delete.html'
    success_url = reverse_lazy('user:user_views')
