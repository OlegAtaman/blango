import blog.views
from django.contrib import admin
from django.urls import path
from django.conf import settings

print(f"Time zone: {settings.TIME_ZONE}")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.index),
    path("post/<slug>/", blog.views.post_detail, name="blog-post-detail")
]
