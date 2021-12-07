from .models import Experience, Footer, Link, Main, Service, Heading, Project
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.conf import settings

# Create your views here.
def index(request):
    if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                subject = form.cleaned_data['subject']
                email_address = form.cleaned_data['email_address'] 
                body = {
                'first_name': f"First Name: {form.cleaned_data['first_name']}",
                'last_name': f"Last Name: {form.cleaned_data['last_name']}",
                'email_address': f"Sender: {form.cleaned_data['email_address']}", 
                'message': f"Message: {form.cleaned_data['message']}", 
                }
                message = "\n".join(body.values())
                try:
                    send_mail(subject, message, email_address, [settings.EMAIL_HOST_USER], fail_silently=False)
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                name= form.cleaned_data['first_name']
                url= "thankyou/?nam={}".format(name)
                return HttpResponseRedirect(url)

    form = ContactForm()
    context = {
        'links': Link.objects.all(),
        'main': Main.objects.get(id=1),
        'about': Heading.objects.get(id=1),
        'servic': Heading.objects.get(id=2),
        'experience': Heading.objects.get(id=3),
        'project': Heading.objects.get(id=4),
        'services': Service.objects.all(),
        'experiences': Experience.objects.all(),
        'projects': Project.objects.all(),
        'form':form,
        'footer': Footer.objects.get(id=1),
    }
    return render(request, "index.html", context)

def thankyou(request):
    if request.method=='GET':
        name=request.GET.get('nam')
    context = {
        'links': Link.objects.all(),
        'main': Main.objects.get(id=1),
        'sender': name,
        'footer': Footer.objects.get(id=1)
    }
    return render(request, 'thankyou.html', context)

def services(request):
    servicing = Service.objects.all().order_by('id')
    paginator = Paginator(servicing, 20)
    page = request.GET.get('page', 1)
    services = paginator.get_page(page)
    context = {
        'links': Link.objects.all(),
        'main': Main.objects.get(id=1),
        'servic': Heading.objects.get(id=2),
        'services': services,
        'footer': Footer.objects.get(id=1)
    }
    return render(request, "services.html", context)

def experience(request):
    experiencing = Experience.objects.all().order_by('id')
    paginator = Paginator(experiencing, 20)
    page = request.GET.get('page', 1)
    experiences = paginator.get_page(page)
    context = {
        'links': Link.objects.all(),
        'main': Main.objects.get(id=1),
        'experience': Heading.objects.get(id=3),
        'experiences': experiences,
        'footer': Footer.objects.get(id=1)
    }
    return render(request, "experience.html", context)

def projects(request):
    projecting = Project.objects.all().order_by('id')
    paginator = Paginator(projecting, 20)
    page = request.GET.get('page', 1)
    projects = paginator.get_page(page)
    context = {
        'links': Link.objects.all(),
        'main': Main.objects.get(id=1),
        'project': Heading.objects.get(id=4),
        'projects': projects,
        'footer': Footer.objects.get(id=1)
    }
    return render(request, "projects.html", context)