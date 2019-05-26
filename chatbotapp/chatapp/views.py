import json

from django.http import HttpResponse
from django.shortcuts import render

from chatapp.models import Profile, Answer, Question


def bot(request):
    args = {}
    if request.method == 'POST' and request.is_ajax():
        if request.POST.get('question') == '1':
            user = Profile.objects.create(name=request.POST.get('answer'))
            next_question_id = int(request.POST.get('question')) + 1
            next_question = Question.objects.get(id=next_question_id)
            args['next_question_id'] = next_question.id
            args['next_question_text'] = next_question.text
            args['user'] = user.id

        else:
            Answer.objects.create(profile_id=int(request.POST.get('user')),
                                text=request.POST.get('answer'),
                                question_id=int(request.POST.get('question'))
                                )
            next_question_id = int(request.POST.get('question')) + 1
            if request.POST.get('question') == '3':
                args['button'] = 'true'
            try:
                next_question = Question.objects.get(id=next_question_id)
                args['next_question_id'] = next_question.id
                args['next_question_text'] = next_question.text
            except:
                args['end'] = 'end'
            args['user'] = request.POST.get('user')
        return HttpResponse(json.dumps(args), content_type='application/javascript; charset=utf8')
    else:
        question = Question.objects.first()
        args['question'] = question
        args['next'] = int(question.id) + 1
        return render(request, 'chatapp/bot.html', args)


def result(request):
    args = {}
    profile = Profile.objects.get(id=int(request.GET.get('user')))
    answers = Answer.objects.filter(profile_id=int(request.GET.get('user')))

    answers_text = answers[2].text
    if (answers_text == 'no'):
        smoker = 'non-smoker'
    else:
        smoker = 'smoker'

    args['answers'] = answers
    args['name'] = profile.name
    args['smoker'] = smoker

    return render(request, 'chatapp/result.html', args)


