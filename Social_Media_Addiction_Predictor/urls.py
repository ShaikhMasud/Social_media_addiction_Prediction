from django.urls import path
from Social_Media_Addiction_Predictor_app.views import predict_stress,home

urlpatterns = [
    path("",home,name="home"),
    path("predict", predict_stress, name="predict_stress")
]
