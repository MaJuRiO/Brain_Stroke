from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import View
from django.http import JsonResponse
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict
from django.db.models import Max
from django.db import transaction
from .models import *
import json
import re

import csv


# Create your views here.
def index(request):
    data = {}
    return render(request, 'index.html', data)
def predicthealth(request):
    if request.method == 'POST':
        data = request.POST.copy()
        body_fat = data.get('body_fat')
        basal_metabolism = data.get('basal_metabolism')
        skeletal_muscle = data.get('skeletal_muscle')
        weight = data.get('weight')
        bmi = data.get('bmi')
        age = data.get('age')
        gender = data.get('gender')
        quantity_activity = data.get('quantity_activity')
        diet = data.get('diet')
        high_blood = data.get('high_blood')
        diabetes = data.get('diabetes')
        drink = data.get('drink')
        
        new = storage_history()
        new.body_fat = body_fat
        new.basal_metabolism = basal_metabolism 
        new.skeletal_muscle = skeletal_muscle
        new.weight = weight
        new.bmi = bmi
        new.age = age
        new.gender = gender
        new.quantity_activity = quantity_activity
        new.diet = diet
        new.high_blood = high_blood
        new.diabetes = diabetes
        new.drink = drink
        
        new.save()
    return render(request, 'predicthealth.html')

def result(request):
    history = storage_history.objects.all().order_by('id').reverse()[:1]
    #preorder = storage_history.objects.filter(quantity__lte=0) 
	# quanlity__lte=0 (หาค่าที่ quantity <= 0 - lte is <= ) (underscore 2 ตัว)
	#quantity__gt=0 (หาค่าที่ quantity > 0 - gt is >)
	#quantity__gte=0 (หาค่าที่ quantity >= 5 - gte is >=)
    # data = {'product':product,'preorder':preorder}
    data = {'history':history}
	
    return render(request, 'resultpredict.html', data)


def export_to_csv(request):
    storage = storage_history.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename; filename=data_export.csv'
    writer = csv.writer(response)
    writer.writerow(['visceral_level', 'body_fat', 'basal_metabolism',
                     'skeletal_muscle', 'weight', 'bmi', 'age', 'gender', 'quantity_activity',
                     'diet', 'high_blood', 'diabetes', 'drink'])
    storage_fields = storage.values_list('visceral_level', 'body_fat', 'basal_metabolism',
                     'skeletal_muscle', 'weight', 'bmi', 'age', 'gender','quantity_activity',
                     'diet', 'high_blood', 'diabetes', 'drink')
    for storage in storage_fields:
        writer.writerow(storage)
    return response

def export_to_csv_one(request):
    storage = storage_history.objects.all().order_by('id').reverse()[:1]
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename; filename=data_export.csv'
    writer = csv.writer(response)
    writer.writerow(['visceral_level', 'body_fat', 'basal_metabolism',
                     'skeletal_muscle', 'weight', 'bmi', 'age', 'gender', 'quantity_activity',
                     'diet', 'high_blood', 'diabetes', 'drink'])
    storage_fields = storage.values_list('visceral_level', 'body_fat', 'basal_metabolism',
                     'skeletal_muscle', 'weight', 'bmi', 'age', 'gender','quantity_activity',
                     'diet', 'high_blood', 'diabetes', 'drink')
    for storage in storage_fields:
        writer.writerow(storage)
    return response