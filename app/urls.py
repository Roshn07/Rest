from django.urls import path
from . import views

urlpatterns = [
   path('',views.hello),
   path('students_c/',views.StudentListView.as_view()),
   path('students_d/',views.RecipeDetailView.as_view()),
   path('students_list',views.list_students),
   path('student_detail/<int:id>/',views.students_detail)
]