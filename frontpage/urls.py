from django.urls import path
from .views import FrontPage


app_name = 'frontpage'


urlpatterns = [
    path(
        route='',
        view=FrontPage.as_view(),
        name='frontpage'
    )
]
