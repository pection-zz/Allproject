from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf.urls.static import static
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, "main.html", context=None)
# Add this view
class AboutPageView(TemplateView):
    template_name = "about.html"

class ContactPageView(TemplateView):
    template_name = "contact.html"