from xml.dom.minidom import Document
from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.projects,name="projects"),
    path('talklawyer',views.talklawyer,name="talk-to-a-lawyer"),
    path('askaquestion',views.askaquestion,name="askaquestion"),
    path('hello-world',views.test,name="hello-world"),
    path('searchlawyer',views.search,name="search"),
    path('aboutus',views.aboutus,name="aboutus"),
    path('lawyer/<str:pk>',views.project,name="lawyer"),    
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)