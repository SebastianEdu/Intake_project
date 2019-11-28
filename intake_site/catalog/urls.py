from django.urls import path
from . import views

urlpatterns = [
	path('brand/<int:pk>', views.BrandDetailView.as_view(), name='brand-detail'),
	path('',views.index,name='index'),
	#path('login/',views.login,name='login'),
	path('cars/', views.CarListView.as_view(), name='cars'),
	path('car/<int:pk>', views.CarDetailView.as_view(), name='car-detail'),	
	path('brands/', views.BrandListView.as_view(), name='brands'),
	path('signup/', views.SignUp.as_view(), name='signup'),

]

urlpatterns += [
    path('car/create/', views.CarCreate.as_view(), name='car_create'),
    path('car/<int:pk>/update/', views.CarUpdate.as_view(), name='car_update'),
    path('car/<int:pk>/delete/', views.CarDelete.as_view(), name='car_delete'),
]