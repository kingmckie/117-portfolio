from django.shortcuts import render, redirect
from .forms import ContactForm
from django.template.loader import render_to_string
from django.core.mail import send_mail

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    if request.method == 'POST':
        form= ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email_from = form.cleaned_data['email']
            message = form.cleaned_data['message']

            html = render_to_string('pages/email.html', request.POST)

            send_mail('message from' + name, message, email_from, ['everal.m.mckie@gmail.com'], html_message=html)

            return redirect('about')
        else:
            print('Not Valid!')
    else:
        form = ContactForm()


    return render(request, 'pages/contact.html', {
        'form' : form
    })