from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .models import Polls
import numpy as np

# Create your views here.


def home(request):
    user = request.user.username
    is_authenticated = request.user.is_authenticated
    polls = Polls.objects.all()
    poll_names = [poll.name for poll in polls]
    poll_names = np.unique(poll_names)
    if is_authenticated:
        owns = []
        for i in polls:
            if user == i.owner:
                owns.append(i.name)
        owns = np.unique(owns)
        return render(request, 'polling_home.html', {'username': user, "poll_names": poll_names, 'owns': owns})

    else:
        return redirect('/login/')


def create_poll(request, username):
    is_authenticated = request.user.is_authenticated
    username = request.user.username
    polls = Polls.objects.all()
    if is_authenticated:
        return render(request, 'create_poll.html', {"username": username, 'polls': polls})
    else:
        return redirect('/login/')


def add(request, username):
    username = request.user.username
    name = request.POST['name']
    question = request.POST['question']
    if not(Polls.objects.filter(questions=question)):
        poll = Polls.objects.create(
            name=name, questions=question, owner=request.user.username)
        poll.save()
    else:
        messages.info(request, 'question already exists')
    return redirect('/polling/'+username+'/create_poll/')


def poll(request, poll_name):
    poll = Polls.objects.filter(name=poll_name)
    questNames = [i.questions for i in poll]
    return render(request, 'poll.html', {'poll_name': poll_name, 'questNames': questNames})


def commit(request):
    poll_name = request.POST['poll_name']
    temp = Polls.objects.filter(name=poll_name)
    question = [i.questions for i in temp]  # list of quest in poll
    for i in question:
        poll = Polls.objects.get(name=poll_name, questions=i)
        answer = request.POST[i]
        if poll.answer == '':
            poll.answer = answer
        else:
            poll.answer += ',' + answer
        poll.save()
    return redirect('/polling/thank-filling/')


def inspection(request, poll_name):
    poll = Polls.objects.filter(name=poll_name)
    questions = [i.name for i in poll]  # list of quests
    answers = [i.answer.split(',') for i in poll]  # list of aswers

    return render(request, 'inspection.html', {'poll_name': poll_name, 'polls': poll})


def thank_filling(request):
    return render(request, 'thank_filling.html')
