from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^our-story$', views.our_story, name='our_story'),
    url(r'^safety-and-insurance/$', views.safety_insurance, name='safety_insurance'),
    url(r'^request-a-quote/$', views.request_quote, name='request_quote'),
    url(r'^travel/$', views.travel, name='travel'),
    url(r'^travel-info/$', views.travel_info, name='travel_info'),
    url(r'^contact-us/$', views.contact_us, name='contact-us'),
    # other pages
    url(r'^testimonials/$', views.testimonials, name='testimonials')
]
