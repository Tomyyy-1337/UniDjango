from django.shortcuts import render

# Create your views here.
from university.models import *
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Q
from django.template import Context, loader

def show_index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def show_aktive_studenten_anzahl(request):
    count = Student.objects.filter(~Q(hoert=None)).count()
    text = 'Es gibt %s active Studenten.' % count
    return HttpResponse(text)

def show_professoren_all(request):
    prof = Professor.objects.all().order_by('name')
    s = ''
    for item in prof:
        s = s + '<tr><td>%s</td><td>%s</td></tr>' % (item.name,item.persnr,)
    text = '<table><tr><th>name</th><th>persnr</th></tr>%s</table>' % s
    return HttpResponse(text)

def show_professoren_all_json(request):
    prof = Professor.objects.all().order_by('name')
    s = ''
    for item in prof:
        s = s + '<tr><td>%s</td><td>%s</td></tr>' % (item.name,item.persnr,)
    text = '<table><tr><th>name</th><th>persnr</th></tr>%s</table>' % s
    return JsonResponse(text, safe=False)

def x_show_aktive_studenten_anzahl(request):
    context = { 
            'stud_count': Student.objects.filter(~Q(hoert=None)).count(), 
        }

    template = loader.get_template('studenten_anzahl.html')
    return HttpResponse(template.render(context))

def x_show_professoren_all(request):
    prof = Professor.objects.all().order_by('name')
    context = {'all_prof': prof,}
    template = loader.get_template('all_prof.html')
    return HttpResponse(template.render(context))

def x_show_professoren_all_json(request):
    prof = Professor.objects.all().order_by('name')
    s = ''
    for item in prof:
        s = s + '<tr><td>%s</td><td>%s</td></tr>' % (item.name,item.persnr,)
    text = '<table><tr><th>name</th><th>persnr</th></tr>%s</table>' % s
    return JsonResponse(text, safe=False)

def show_dozenten_anzahl(request):
    count = Professor.objects.count()
    text = 'Wir haben %s Dozenten.' % count
    return HttpResponse(text,content_type="text/plain")

