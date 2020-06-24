from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse

from .models import Medicine, Doctor, Patient

def index(request):
    all_doctors = Doctor.objects.all()
    return render(request, 'doctors/list.html', {'all_doctors': all_doctors})
    
    
def doc_info(request, doctor_id):
    try:
        a = Doctor.objects.get(id = doctor_id)
    except:
        raise Http404('Статья не найдена!')
        
    latest_comments_list = a.comment_set.order_by('-id')[:10]
        
    return render(request, 'doctors/detail.html', {'doctor': a, 'latest_comments_list': latest_comments_list})
    
def leave_comment(request, docotor_id):
    try:
        a = Doctor.objects.get(id = doctor_id)
    except:
        raise Http404('Статья не найдена!')
        
    a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])
    
    return HttpResponseRedirect(reverse('doctors:detail', args = (a.id,)))