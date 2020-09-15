from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls import url

urlpatterns = [
	#Leave as empty string for base url
	# path('', views.store, name="store"),
	url(r"^$", views.HomePageView.as_view()),
    url(r"^about/$", views.AboutPageView.as_view()), # Add this /about/ route
    url(r"^contact/$", views.ContactPageView.as_view()), # Add this /about/ route

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)