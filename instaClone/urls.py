
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", include("feed.urls")),
    path("admin/", admin.site.urls),
    path('register/', user_views.register, name="register"),

    path('profile/edit', user_views.editProfile, name='editProfile'),
    path('shopping-cart/', user_views.shoppingCart, name='shopping-cart'),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
