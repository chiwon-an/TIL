from django.urls import path
from . import views  # ← 모듈로 임포트
urlpatterns = [
    path('', views.PostListCreateView.as_view()),
    path('<int:pk>/', views.PostRetrieveUpdateDestroyView.as_view()),
]