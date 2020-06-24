from django.views.generic import TemplateView
from django.shortcuts import render

class IndexPageView(TemplateView):
    template_name = 'main/index.html'


class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'

class NotificationsView(TemplateView):
    template_name = 'main/notifications.html'

def createEvent(request):
    pagetitle = "Hello World"
    if request.method == 'POST':
        event_title = request.POST.get('event_title')
        event_description = request.POST.get('event_description')
        print(event_title)
        print(event_description)

    return render(request, 'main/createEvent.html', {'pagetitle':pagetitle})