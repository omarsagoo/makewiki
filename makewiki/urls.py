from django.contrib import admin
from django.urls import path, include

"""
CHALLENGES:
    1. Uncomment the path() for the wiki app below. Use it to direct any request (except `/admin` URLs)
        to the the `wiki` app's URL configuration. Use the above docstring to guide you if you feel stuck.
    2. Make sure Django doesn't give you any warnings or errors when you execute `python manage.py runserver`.
"""
urlpatterns = [
    # Admin Site
    path('admin/', admin.site.urls),

    # Wiki App
    path('', include('wiki.urls')),
]
