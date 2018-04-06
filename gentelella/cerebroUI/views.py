from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import datetime
from .models import *
from django.contrib.auth.models import User

now = datetime.datetime.now()
def find_username(r):
    try:
        username = r.user.get_full_name
        return username
    except:
        return 'Anonymous'

def data_filter_by_status(data, status='None'):
    if status in ["Automatched", "Unmatched", "Nomatched"]:
        return data.objects.filter(status=status)
    else:
        return data.objects.all()

#will change
def index(request):
    context = {'time': now, 
                'object_list': data_filter_by_status(SrcData),
                'object_list_auto': data_filter_by_status(SrcData, "Automatched"),
                'object_list_un': data_filter_by_status(SrcData, "Unmatched"),
                'object_list_no': data_filter_by_status(SrcData, "Nomatched"),
                'current_user': find_username(request)}
    # print ("######"+find_username(request))
    template = loader.get_template('app/tables_dynamic.html')
    return HttpResponse(template.render(context, request))


def gentella_html(request):
    context = { 'time': now, 
                'object_list': data_filter_by_status(SrcData),
                'object_list_auto': data_filter_by_status(SrcData, "Automatched"),
                'object_list_un': data_filter_by_status(SrcData, "Unmatched"),
                'object_list_no': data_filter_by_status(SrcData, "Nomatched"),
                'current_user': find_username(request)}
    # The template to be loaded as per gentelella.
    # All resource paths for gentelella end in .html.
    # print ("######"+find_username(request))
    # Pick out the html file name from the url. And load that template.
    load_template = request.path.split('/')[-1]
    # print ("YOUR REQUEST PATH: "+request.path)
    template = loader.get_template('app/' + load_template)
    return HttpResponse(template.render(context, request))
 

# def CerebroTableView(request):
#     queryset = SrcData.objects.all()
#     context = {
#         "object_list":queryset

#     }