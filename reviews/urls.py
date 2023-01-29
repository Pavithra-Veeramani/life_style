from django.urls import path
from . import views


urlpatterns = [
    path(
        'create-review/<int:product_id>/',
        views.create_review, name='create_review'),

]
