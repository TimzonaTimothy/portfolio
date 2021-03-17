from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from django.core.mail import send_mail
from django.http import HttpResponse
# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        context['file'] = FilesAdmin.objects.all()
        context['services'] = Service.objects.all()
        context['works'] = RecentWork.objects.all()
        context['client'] = Client.objects.all()
        return context

def contact(request):
    if request.method == "POST":
        massage_name = request.POST['massage_name'] 
        massage_email = request.POST['email']
        massage = request.POST['massage']
        #send mai
        send_mail = (
            massage_name,
            massage_email,
            massage,['arizonatymothy@gmail.com','timzonatimothy@gamil.com']
        )
        return render(request, 'contact.html', {'massage_name':massage_name,'massage_email':massage_email,'massage':massage})

    else:
        return render(request, 'contact.html', {})

def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path, 'rb')as fh:
            response=HttpResponse(fh.read(),content_type='application/adminupload')
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response
    
    raise Http404