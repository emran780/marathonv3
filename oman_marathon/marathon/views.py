from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ContactUsForm, RunnerLoginForm, RunnerUpdateForm
from .models import Runner, ContactUsMessage
from django.http import HttpResponse




def welcome(request):
    return render(request, 'welcome.html')

def about(request):
    return render(request, 'about.html')

def login_user(request):
    if request.method == 'POST':
        form = RunnerLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('runner_dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid form submission. Please check the form and try again.')
    else:
        form = RunnerLoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def logout_user(request):
    logout(request)
    messages.info(request, 'Logout successful!')
    return redirect('welcome')



def past_events(request):
    return render(request, 'past_events.html')


def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            # Save the form data to the database or take appropriate action
            form.save()
            messages.success(request, 'Your feedback has been submitted!')
            return redirect('welcome')
        else:
            messages.error(request, 'There was an error in the form submission. Please check the form and try again.')
    else:
        form = ContactUsForm()
    return render(request, 'contact_us.html', {'form': form})



@login_required
def runner_dashboard(request):
    runner = get_object_or_404(Runner, user=request.user)
    return render(request, 'runner_dashboard.html', {'runner': runner})


@login_required
def update_runner(request):
    runner = get_object_or_404(Runner, user=request.user)

    if request.method == 'POST':
        form = RunnerUpdateForm(request.POST, instance=runner)
        if form.is_valid():
            form.save()
            messages.success(request, 'Runner information updated successfully!')
            return redirect('runner_dashboard')
        else:
            messages.error(request, 'Invalid form submission. Please check the form and try again.')
    else:
        form = RunnerUpdateForm(instance=runner)

    return render(request, 'update_runner.html', {'form': form})



@login_required
def delete_runner(request, runner_id):
    runner = get_object_or_404(Runner, id=runner_id, user=request.user)
    
    if request.method == 'POST':
        runner.delete()
        messages.success(request, 'Runner deleted successfully!')
        # return redirect('runner_dashboard')
        return redirect('welcome')


    return render(request, 'delete_runner.html', {'runner': runner})