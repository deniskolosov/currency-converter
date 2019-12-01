from django.urls import include, path
from rest_framework.routers import DefaultRouter
from fetcher.views import RatesViewSet, HomePageView, LatestRate

router = DefaultRouter()
router.register(r'rates', RatesViewSet, base_name='rates')


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('latest', LatestRate.as_view(), name='latest'),
    path('', include(router.urls)),
]
