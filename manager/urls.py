from django.urls import path
from manager import views


urlpatterns = [
    path('',views.home),
    path('login/',views.login),
    path('register/',views.register),
    path('book/',views.books),
    path('add/',views.add),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.delete),
]