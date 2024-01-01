from django.urls import path
from InfoAPP import views

urlpatterns = [
    path('', views.home),
    path('principalhome/', views.principalhome, name='principalhome'),
    path('facultyhome/', views.facultyhome, name='facultyhome'),
    path('principallogin/', views.principallogin),
    path('facultylogin/', views.facultylogin),
    path('facultydata/', views.facultydata),
    path('studentdata/', views.studentdata),
    path('addfacultydata/', views.addfacultydata),
    path('addstudentdata/', views.addstudentdata),
    path('deletefaculty/', views.deletefaculty),
    path('deletefacultyid/<int:id>', views.deletefacultyid),
    path('deletestudent/', views.deletestudent),
    path('deletestudentid/<int:id>', views.deletestudentid),
    path('editstudent/', views.editstudent),
    path('editstudentid/<int:id>', views.editstudentid),
    path('editfaculty/', views.editfaculty),
    path('editfacultyid/<int:id>', views.editfacultyid),
]
