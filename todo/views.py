from datetime import date

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import ToDoItem
from django.conf import settings
from django.core.mail import send_mail


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )
        login(request, user)
        subject = 'welcome to my first website'
        message = f'Hi {user.username}, thank you for registering in my website.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email, ]
        send_mail(subject, message, email_from, recipient_list)
        return redirect("/dashboard/")
    return render(request, "signup.html")


class AllToDos(ListView):
    model = ToDoItem
    template_name = "todo/index.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(due_date__gte=date.today())


class TodayToDos(ListView):
    model = ToDoItem
    template_name = "todo/today.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(due_date=date.today())
