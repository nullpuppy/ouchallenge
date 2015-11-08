from django.conf.urls import url
from itemPrices import views

urlpatterns = [
    url(r'^item-price-service/$', views.ItemPriceService.as_view()),
]
