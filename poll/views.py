from django.shortcuts import render
from poll.models import *
from django.http import Http404,HttpResponse

# Create your views here.
def index(request):
    context = {}
    question = Question.objects.all()
    context['title'] = 'polls'
    context['questions'] = question
    return render(request,'poll/index.html' , context)


def details(request,id=None):
    context = {}
    try:
        question = Question.objects.get(id=id)
    except:
        raise Http404
    context['question'] = question
    return render(request,'poll/details.html' , context)
        

def poll(request,id=None):
    if request.method == "GET":
        try:
            question = Question.objects.get(id=id)
        except:
            raise Http404
        context = {}
        context['question'] = question
        return render(request,"poll/poll.html",context)
    if request.method == "POST":
        user_id =1
        data = request.POST
        rel = Answer.objects.create(user_id = user_id ,choice_id=data['choice'])
        if rel:
            return HttpResponse("Your vote is Succesfull")
        else:
            return HttpResponse("Your vote is Succesfull")