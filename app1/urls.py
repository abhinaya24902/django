from django.urls import path
from.import views

urlpatterns = [
    path('',views.set_session),
    path('gets/',views.get_session),
    path('setc/',views.set_cookie),
    path('getc/',views.get_cookie),
    path('delts/',views.delete_session),
    path('deltc/',views.delete_cookie),

]
