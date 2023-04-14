import debug_toolbar

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django_registration.backends.activation.views import RegistrationView

import blog.views, blango_auth.views
from blango_auth.forms import BlangoRegistrationForm

print(f"Time zone: {settings.TIME_ZONE}")
urlpatterns = [
    path("api/v1/", include("blog.api.urls")),
    path('admin/', admin.site.urls),
    path('', blog.views.index),
    path('ip/', blog.views.get_ip),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/profile/", blango_auth.views.profile, name="profile"),
    path("post/<slug>/", blog.views.post_detail, name="blog-post-detail"),
    path(
        "accounts/register/",
        RegistrationView.as_view(form_class=BlangoRegistrationForm),
        name="django_registration_register",
    ),
    path("accounts/", include("django_registration.backends.activation.urls")),
    path("accounts/", include("allauth.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ]
