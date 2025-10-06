from django.urls import path

from . import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('serie',views.SeriesView.as_view(),name='series'),
    path('serie/<int:serie_id>',views.SerieDetailView.as_view()),
    path('category', views.CategoryListCreateView.as_view(), name='categories'),
    path('category/<int:pk>', views.CategoryDetailView.as_view(), name='category-detail'),

]
