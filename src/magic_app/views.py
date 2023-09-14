from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import FormView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.db import transaction
import random
from django.contrib import messages
from service.service import plural
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *

class LoginUserView(FormView):
    form_class = LoginForm
    template_name = 'pages/login.html'
    success_url = reverse_lazy('magic_app:question')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
    
    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

class QuestionView(LoginRequiredMixin, FormView):
    form_class = QuestionForm
    template_name = 'pages/question.html'
    success_url = reverse_lazy('magic_app:question')

    def handle_no_permission(self):
        return redirect('magic_app:login')

    @transaction.atomic
    def post(self, request, *args, **kwargs):
            form = self.get_form()
            if form.is_valid():
                random_answer = random.randint(0, len(QuestionUser.ANSWER)-1)
                question = Question.objects.filter(question=form.data['question']).first()
                if not question:
                    question = Question.objects.create(question=form.data['question'])
                question_answer = QuestionUser.objects.create(question=question, user=self.request.user, answer=f'{random_answer}')
                count_question = QuestionUser.objects.filter(question=question).count()
                if count_question == 1:
                    self.message = f'Вы первый кто задал этот вопрос, шар вам ответил: "{question_answer.get_answer_display()}"'
                else:
                    self.message = f'Пользователи задали этот вопрос уже {count_question} {plural(count_question)}. Для вас магический шар ответил: "{question_answer.get_answer_display()}"'
                return self.form_valid(form)
            else:
                return self.form_invalid(form)

    def get_success_url(self, **kwargs):
        messages.add_message(self.request, messages.INFO, self.message)
        return reverse_lazy('magic_app:question')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['history_question'] = QuestionUser.objects.filter(user=self.request.user).order_by('-date')[:20]        
        return context


