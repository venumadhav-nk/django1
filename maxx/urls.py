from django.urls import path

from . import views

urlpatterns =[
    path('fun/',views.fun),
    path('fun2',views.fun2,name='fun2'),
    path('nk/<str:fath>/<str:son>',views.nk),
    path("kow/<str:p_name>/<str:b_name>",views.kow),
    path("base/",views.base),
    path("page1/<str:baby>/<str:butter>",views.page1),
    path("page2/<str:dady>/<str:son>",views.page2),
    path("page3/<str:pop>/<str:top>",views.page3),
    path('info/',views.info),
    path("calsi/",views.calsi),
    path('wish/<str:father>/<str:son>/',views.wish),
    path('rhyme1/<str:butter>/<str:baby>/',views.rhyme1),
    path('rhyme2/<str:pop>/<str:top>/',views.rhyme2),
    path('rhyme3/<str:ringa>/<str:rose>/',views.rhyme3),
    
]