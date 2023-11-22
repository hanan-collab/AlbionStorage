from django.urls import path
from main.views import create_product_flutter, show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, decrement_amount, increment_amount, delete_product
from main.views import get_product_json, add_product_ajax, get_product_count, get_balance
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('decrement_amount/<int:id>/', decrement_amount, name='decrement_amount'),
    path('increment_amount/<int:id>/', increment_amount, name='increment_amount'),
    path('delete_product/<int:id>/', delete_product, name='delete_product'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('get-product-count/', get_product_count, name='get_product_count'),
    path('get-balance/', get_balance, name='get_balance'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]