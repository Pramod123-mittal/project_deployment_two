from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserForm
from django.http import HttpResponseRedirect
from .models import profile
from django.urls import reverse,reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from ems.decorators import admin_hr_required, admin_only


from django.utils.decorators import method_decorator


# from django.contrib.auth import User
# Create your views here.
def user_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # return HttpResponseRedirect(reverse('user_success'))
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
            return HttpResponseRedirect(reverse('employee_list'))
        else:
            context['error'] = 'please provide correct credentials !!'
            return render(request, 'auth/login.html', context)
    else:
        return render(request, 'auth/login.html', context)


def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/login')


@login_required(login_url='/login/')
def success(request):
    context = {}
    context['user'] = request.user
    return render(request, 'auth/success.html', context)


@login_required(login_url='/login/')
def employee_list(request):
    print(request.role)
    context = {}
    context['users'] = User.objects.all()
    context['title'] = 'Employees'
    return render(request, 'employee/index.html', context)


@login_required(login_url='/login/')
def employee_details(request, id=None):
    context = {}
    context['user'] = User.objects.get(id=id)
    # select * from user where id = id;
    return render(request, 'employee/details.html', context)


@login_required(login_url='/login/')
# @role_required(allowed_roles=['Admin', 'HR'])
@admin_only
def employee_add(request):
    context = {}
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        context['user_form'] = user_form
        if user_form.is_valid():

            user_form.save()
            return HttpResponseRedirect(reverse('employee_list'))
        else:
            return render(request, 'employee/add.html', context)
    else:
        user_form = UserForm()
        context['user_form'] = user_form
        return render(request, 'employee/add.html', context)


@login_required(login_url='/login/')
@admin_only
def employee_edit(request, id=None):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse("employee_list"))
        else:
            return render(request, 'employee/edit.html', {'user_form': user_form})
    else:
        user_form = UserForm(instance=user)
        return render(request, 'employee/edit.html', {'user_form': user_form})


@login_required(login_url='/login/')
def employee_delete(request, id=None):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.delete()
        return HttpResponseRedirect(reverse('employee_list'))
    else:
        context = {}
        context['user'] = user
        return render(request, 'employee/delete.html', context)


class ProfileUpdate(UpdateView):
    fields = ['designation','salary','picture']
    template_name = 'auth/update_profile.html'
    success_url = reverse_lazy('my_profile')
    def get_object(self):
        return self.request.user.profile


class MyProfile(DetailView):
    template_name = 'auth/profile.html'
    def get_object(self):
        return self.request.user.profile