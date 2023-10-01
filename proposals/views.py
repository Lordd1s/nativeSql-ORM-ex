from django.shortcuts import render
from proposals import models
from django.db import connection

# Create your views here.
def homepage(request):
    if request.method == 'GET':
        return render(request, 'homepage.html')
    elif request.method == 'POST':

        name = request.POST.get('name')
        contact = request.POST.get('contact')
        title = request.POST.get('title')
        description = request.POST.get('desc')
        switch = request.POST.get('switch')

        if name == '':
            return render(request, "homepage.html", context={"error": "Ошибка!"})

        context = {"message": "Ваше предложение(жалоба) принято! Пожалуйста ждите обратной связи!"}

        if switch is None:
            props = models.Proposes.objects.create(name=name, contact=contact, title=title, description=description)
        elif switch == 'on':
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO proposals_proposes (name, contact, title, description) VALUES (?, ?, ?, ?)", (name, contact, title, description))
        else:
            context = {"error": "Ошибка!"}

        return render(request, "homepage.html", context=context)