from django.urls import path, include

from rest_framework.routers import DefaultRouter
from student import views


router = DefaultRouter()
router.register('profile',views.UserProfileViewSet)
router.register('complaint',views.UserComplaintViewSet)

urlpatterns = [
    path('login/',views.UserLoginApiView.as_view()),
    path('',include(router.urls)),
    ##################################
    # path('accounts/', include('rest_registration.api.urls')),
]
