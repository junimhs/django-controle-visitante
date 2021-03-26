from django.urls import path
from visitors.views import register_visitor, get_visitor, finish_visitor

urlpatterns = [
    path('create/', register_visitor, name='visitor.register'),
    path('info/<int:id>/', get_visitor, name='visitor.info'),
    path('finish/<int:id>/', finish_visitor, name="visitor.finish")
]
