from rest_framework import routers
from .views import (
    UserViewSet, CharityViewSet, DonorViewSet, DonationViewSet,
    CartViewSet, CartedDonationViewSet, OrderViewSet,
    CategoryViewSet, DonationCategoryViewSet
)

router = SimpleRouter()

router.register('users', UserViewSet)
router.register('charities', CharityViewSet)
router.register('donors', DonorViewSet)
router.register('donations', DonationViewSet)
router.register('carts', CartViewSet)
router.register('carted_donations', CartedDonationViewSet)
router.register('orders', OrderViewSet)
router.register('categories', CategoryViewSet)
router.register('donation_categories', DonationCategoryViewSet)

urlpatterns = router.urls