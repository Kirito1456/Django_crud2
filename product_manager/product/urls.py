from django.urls import path

from. import views
from product_manager.settings import DEBUG, STATIC_ROOT, STATIC_URL, MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add-product'),
    path('update/<int:product_id>', views.update_product),
    path('delete/<int:product_id>', views.delete_product),
]

if DEBUG: 
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)