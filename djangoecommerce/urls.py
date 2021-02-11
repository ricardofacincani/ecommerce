"""djangoecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.urls import path, include
from django.contrib import admin

# from django.urls import path
from django.conf import settings
from core import views
from django.views.static import serve as serve_static


urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^contato/$", views.contact, name="contact"),
    url(r"^catalogo/", include(("catalog.urls", "catalog"), namespace="catalog")),
    # url(r'^reviews/', include(('reviews.urls', 'reviews'), namespace='reviews')),
    url(r"^admin/", admin.site.urls),
]


# urlpatterns = [
#    url(r"^$", views.index, name="index"),
#    path("contato/", views.contact, name="contact"),
#    url(r"^catalogo/", include(("catalog.urls", "catalog"), namespace="catalog")),
#    path("admin/", admin.site.urls),
# ]
