from django.urls import path
import silic.views
urlpatterns = [
    path('',silic.views.home,name = 'home'),
    path('home',silic.views.home,name = 'home'),
    path('register',silic.views.register,name = 'register'),
    path('login',silic.views.login,name = 'login'),
    path('logout', silic.views.logout, name='logout'),
    path('customer_home', silic.views.customer_home, name='customer_home'),
    path('admin_home', silic.views.admin_home, name='admin_home'),
    path('news',silic.views.news,name = 'news'),



    path('nbs', silic.views.nbs, name='nbs'),
    path('view_band_style', silic.views.view_band_style, name='view_band_style'),
    path('edit_band_style/<id>', silic.views.edit_band_style, name='edit_band_style'),
    path('delete_band_style/<id>', silic.views.delete_band_style, name='delete_band_style'),

    path('nfs', silic.views.nfs, name='nfs'),
    path('view_font_style', silic.views.view_font_style, name='view_font_style'),
    path('edit_font_style/<id>', silic.views.edit_font_style, name='edit_font_style'),
    path('delete_font_style/<id>', silic.views.delete_font_style, name='delete_font_style'),

    path('add_product/<id>', silic.views.add_product, name='add_product'),
    path('view_product/<id>', silic.views.view_product, name='view_product'),
    path('edit_product/<id>', silic.views.edit_product, name='edit_product'),
    path('delete_product/<id>', silic.views.delete_product, name='delete_product'),

    path('view_prdct_cus/<id>/<idg>', silic.views.view_prdct_cus, name='view_prdct_cus'),
    path('ord_product', silic.views.ord_product, name='ord_product'),
    path('Remove_order/<id>/<idm>/<idt>', silic.views.Remove_order, name='Remove_order'),
    path('ch_out', silic.views.ch_out, name='ch_out'),
    path('ch_out1', silic.views.ch_out1, name='ch_out1'),



    path('new_category', silic.views.new_category, name='new_category'),
    path('view_category', silic.views.view_category, name='view_category'),
    path('edit_category/<id>', silic.views.edit_category, name='edit_category'),
    path('delete_category/<id>', silic.views.delete_category, name='delete_category'),
    path('new_band_size', silic.views.new_band_size, name='new_band_size'),
    path('view_band_size', silic.views.view_band_size, name='view_band_size'),
    path('edit_band_size/<id>', silic.views.edit_band_size, name='edit_band_size'),
    path('delete_band_size/<id>', silic.views.delete_band_size, name='delete_band_size'),

    path('new_clipart', silic.views.new_clipart, name='new_clipart'),
    path('view_clipart', silic.views.view_clipart, name='view_clipart'),
    path('delete_clipart/<id>', silic.views.delete_clipart, name='delete_clipart'),

    path('new_price', silic.views.new_price, name='new_price'),
    path('view_price', silic.views.view_price, name='view_price'),
    path('edit_band_price/<id>', silic.views.edit_band_price, name='edit_band_price'),
    path('delete_band_price/<id>', silic.views.delete_band_price, name='delete_band_price'),

    path('new_ship', silic.views.new_ship, name='new_ship'),
    path('view_ship', silic.views.view_ship, name='view_ship'),
    path('edit_ship/<id>', silic.views.edit_ship, name='edit_ship'),
    path('delete_ship/<id>', silic.views.delete_ship, name='delete_ship'),

    path('new_delivery', silic.views.new_delivery, name='new_delivery'),
    path('view_delivery', silic.views.view_delivery, name='view_delivery'),
    path('edit_delivery/<id>', silic.views.edit_delivery, name='edit_delivery'),
    path('delete_delivery/<id>', silic.views.delete_delivery, name='delete_delivery'),

    path('pre_orders', silic.views.pre_orders, name='pre_orders'),
    path('delete_pre_orders', silic.views.delete_pre_orders, name='delete_pre_orders'),
    path('delete_pre_orderss/<id>', silic.views.delete_pre_orderss, name='delete_pre_orderss'),

    path('ord_cus_band', silic.views.ord_cus_band, name='ord_cus_band'),
    path('view_cart', silic.views.view_cart, name='view_cart'),
    path('delete_cart/<id>', silic.views.delete_cart, name='delete_cart'),
    path('checkout_cus_band', silic.views.checkout_cus_band, name='checkout_cus_band'),

    path('band_cust_orders', silic.views.band_cust_orders, name='band_cust_orders'),
    path('delete_band_cust_orders', silic.views.delete_band_cust_orders, name='delete_band_cust_orders'),
    path('delete_cust_band_orders/<id>', silic.views.delete_cust_band_orders, name='delete_cust_band_orders'),
    path('feedback', silic.views.feedback, name='feedback'),
    path('feedbak', silic.views.feedbak, name='feedbak'),
    path('delete_feedback/<id>', silic.views.delete_feedback, name='delete_feedback'),
    path('faq', silic.views.faq, name='faq'),
    path('faqs', silic.views.faqs, name='faqs'),
    path('quott_disc/<id>', silic.views.quott_disc, name='quott_disc'),
    path('delete_quot/<id>', silic.views.delete_quot, name='delete_quot'),
    path('delete_quotm/<id>', silic.views.delete_quotm, name='delete_quotm'),
    path('quott_req', silic.views.quott_req, name='quott_req'),

    path('quott', silic.views.quott, name='quott'),
    path('view_all_products', silic.views.view_all_products, name='view_all_products'),
    path('quott1', silic.views.quott1, name='quott1'),
    path('customers', silic.views.customers, name='customers'),
    path('block_cust/<id>', silic.views.block_cust, name='block_cust'),
    path('open_cust/<id>', silic.views.open_cust, name='open_cust'),

    path('my_prof', silic.views.my_prof, name='my_prof'),
    path('about', silic.views.about, name='about'),
    path('abb', silic.views.abb, name='abb'),
    path('contact', silic.views.contact, name='contact'),
    path('g_m', silic.views.g_m, name='g_m'),
    path('delete_g_msg/<id>', silic.views.delete_g_msg, name='delete_g_msg'),
    path('del_faq', silic.views.del_faq, name='del_faq'),
    path('delete_faq/<id>', silic.views.delete_faq, name='delete_faq'),

    path('view_cus_band_orders', silic.views.view_cus_band_orders, name='view_cus_band_orders'),
    path('view_pre_cus_ord/<id>', silic.views.view_pre_cus_ord, name='view_pre_cus_ord'),
    path('view_quotations_cust', silic.views.view_quotations_cust, name='view_quotations_cust'),
    path('price_chart', silic.views.price_chart, name='price_chart'),
    path('del_quot', silic.views.del_quot, name='del_quot'),
    path('del_qtt/<id>', silic.views.del_qtt, name='del_qtt'),
    ]