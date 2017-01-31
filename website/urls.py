from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home$', views.index, name='home'),
    url(r'^our-story$', views.our_story, name='our_story'),
    url(r'^safety-and-insurance/$', views.safety_insurance, name='safety_insurance'),
    url(r'^request-a-quote/$', views.request_quote, name='request_quote'),
    url(r'^request-a-quote/(?P<details>[\w]+)$', views.request_quote, name='request_quote'),
    url(r'^travel/$', views.travel, name='travel'),
    url(r'^travel/(?P<year_month>[0-9\-]+)$', views.travel, name='travel'),
    url(r'^category/(?P<category_id>[0-9]+)/travels/$', views.category_travels, name='category_travels'),
    url(r'^trip/(?P<trip_id>[0-9]+)/$', views.view_trip, name='trip'),
    url(r'^event/(?P<event_id>[0-9]+)/$', views.view_event, name='event'),
    url(r'^travel-info/$', views.travel_info, name='travel_info'),
    url(r'^contact-us/$', views.contact_us, name='contact-us'),
    # other pages
    url(r'^testimonials/$', views.testimonials, name='testimonials')
]
