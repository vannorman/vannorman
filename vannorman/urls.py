from django.conf.urls import *

import vannorman.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'vannorman.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),



	url(r'^$', vannorman.views.home),
        url(r'^md/$', vannorman.views.render_md_blog),
	url(r'^blog/$', vannorman.views.blog_base), 
	url(r'^lotus/?$', vannorman.views.simple_page('lotus.html')), 
	url(r'^base/$', vannorman.views.simple_page('base.html')), 
	url(r'^resume/$', vannorman.views.simple_page('resume.html')), 
	url(r'^portfolio/$', vannorman.views.simple_page('portfolio.html')), 
	url(r'^address/$', vannorman.views.simple_page('address.html')), 
	url(r'^blog/(.*)$', vannorman.views.blog), 
	url(r'^test/$', vannorman.views.test), 
	url(r'^jammer/$', vannorman.views.jammer), 
	url(r'^.well-known/acme-challenge/p_LTkY9QHhcECb6Lv1UZWYQ6rawjuQLnUAdBdZZE9kk', vannorman.views.file_a),
	url(r'^.well-known/acme-challenge/v9b5S4UbuLtvh_PwuhqjfOUnVfiulJSmFCYkNHtD6mA', vannorman.views.file_b),


	url(r'^messages/whatyouwant$', vannorman.views.simple_page('messages/isthiswhatyouwant.html')), 




]
