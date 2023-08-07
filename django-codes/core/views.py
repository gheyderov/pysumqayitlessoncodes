from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from stories.models import Category
from core.forms import ContactForm
from django.contrib import messages
from django.views.generic import CreateView
from core.models import Contact

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data = request.POST)
        if form.is_valid():
            messages.add_message(request, messages.SUCCESS, "Successfully sent!")
            form.save()
            return redirect(reverse_lazy('contact'))
    context = {
        'form' : form
    }
    return render(request, 'contact.html', context)


class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.add_message(self.request, messages.SUCCESS, "Successfully sent!")
        return super().form_valid(form)