'''
Created on Jun 1, 2018

@author: student
'''

'''

# urls.py
from appname.views import (
              AboutView,
              ContactView,
              )

urlpatterns = patterns('',
    url(r'^$', 'appname.views.home_view', name='home'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^profile/(?P<username>[\w.@+-]+)/$', 'appname.views.profile_detail', name='profile'),
    url(r'^article/(?P<slug>[\w-]+)/$', 'appname.views.article_detail', name='article'),
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

Username (user's username)
Regex:
(?P<username>[\w.@+-]+)

Example:
Parameters:
username = 'email@email.com' 
or 
username = 'myusername' ## this paramater can be either email or username fields

Query:
object = UserModel.objects.get(username=username)

Url:
url(?P<username>[\w.@+-]+)$', 'appname.views.show_user'),

View:
def show_user(request, username):
    ...
    return ...

Live usage:
yourdomain.com/email@email.com/
or
yourdomain.com/myusername/

Digits and Dates (through digits)

4 Digits like 2015
(?P<year>\d{4})

2 Digits like 12
(?P<month>\d{2})

Any Digits like 1231 or 123438192
(?P<article_id>\d+)

(r'^articles/(?P<year>\d{4})/$', views.year_archive),
(r'^articles/(\d{4})/(?P<month>\d{2})/$', views.month_archive),
(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/(?P<article_id>\d+)/$', views.article_detail),

View:
ef year_archive(request, year):
    return ..

def month_archive(request, month):
    return ..

def article_detail(request, year, month, article_id):
    ...
    return ...

yourdomain.com/2015/
yourdomain.com/2015/03/
yourdomain.com/2015/03/21/    
'''

