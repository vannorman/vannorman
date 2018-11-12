from django.conf.urls import *

import vannorman.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'vannorman.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),



	url(r'^$', vannorman.views.home),
	url(r'^blog/$', vannorman.views.blog_base), 
	url(r'^base/$', vannorman.views.simple_page('base.html')), 
	url(r'^resume/$', vannorman.views.simple_page('resume.html')), 
	url(r'^rl/$', vannorman.views.simple_page('rl.html')), 
	url(r'^lunar/$', vannorman.views.lunar), # ('lunar.html')), 
	url(r'^portfolio/$', vannorman.views.simple_page('portfolio.html')), 
	url(r'^address/$', vannorman.views.simple_page('address.html')), 
	url(r'^blog/(.*)/$', vannorman.views.blog), 
	url(r'^.well-known/acme-challenge/p_LTkY9QHhcECb6Lv1UZWYQ6rawjuQLnUAdBdZZE9kk', vannorman.views.file_a),
	url(r'^.well-known/acme-challenge/v9b5S4UbuLtvh_PwuhqjfOUnVfiulJSmFCYkNHtD6mA', vannorman.views.file_b),


	url(r'^messages/whatyouwant$', vannorman.views.simple_page('messages/isthiswhatyouwant.html')), 




]
