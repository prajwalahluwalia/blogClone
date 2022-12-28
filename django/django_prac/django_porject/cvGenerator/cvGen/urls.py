from django.urls import path
from cvGen import views
from django_pdfkit import PDFView

app_name = 'cvGen'

urlpatterns = [
    path('<int:pk>/', views.resume, name='resume'),
    path('create/', views.CreateCv.as_view(), name='create'),
    path('all/', views.cvList, name='all')
    # path('resume/<int:pk>', PDFView.as_view(template_name='cvGen/resume.html'), name='resume')
]