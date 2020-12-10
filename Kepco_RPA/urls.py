#from django.urls import path
from django.urls import path

from Kepco_RPA import views
urlpatterns=[
    path('',views.start,name='start'),
    path('contents/', views.contents, name='contents'),
    path('step1/',views.step1,name='step1'),
    path('step2/',views.step2,name='step2'),
    path('contents2/',views.contents2, name='contents2')
]