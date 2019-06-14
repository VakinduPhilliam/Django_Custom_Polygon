from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter


from .views import ServiceAreaViewSet, ProviderViewSet


# Set up Router



router = DefaultRouter()

router.register('providers', ProviderViewSet)

router.register('service-areas', ServiceAreaViewSet)




urlpatterns = [
    
url(r'^api/v1/', include(router.urls)),

]
