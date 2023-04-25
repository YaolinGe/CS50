from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }    
    return render(request, "polls/index.html", context)
    # return HttpResponse(template.render(context, request))
    # output = ",    \n ".join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # try: 
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist: 
    #     raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})
    # return HttpResponse("You're looking at question %s. " % question_id)

def results(request, question_id):
    # return HttpResponseNotFound()
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try: 
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": question, 
            "error_message": "You didn't select a choice.", 
        }, 
        )
    else: 
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id, )))
    # return HttpResponse("You're voting on question %s. " % question_id)