from django.urls import path
from .views import BookList
#Task 2
from .views import BookViewSet
from rest_framework.routers import DefaultRouter
from django.urls import include
#Task 3: 
from .views import UserViewSet, TokenObtainView)
from .views import AuthenticatedViewset, AdminViewSet, PublicView
#create and register routers

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename = 'book_all')
router.register(r'users_all', UserViewSet, name = 'user_all')

#create urlpatterns

urlpatterns = [
        #task1: Route for BookList View (ListViewAPI)
        path('books/', BookList.as_view(), name = 'book-list'),
        #task2: Include the generated router URLS for BookViewSet (all CRUD operations)
        path('', include(router.urls)), #includes all routes created and registered with the router whcih is automatic
        #Task3: Token retrieval through username and password
        path('api/token/', obtain_auth_token, name='obtain-token'),
        #Task 3b: authentication of users with tokens for a view
        path('api/user-auth/', include('rest_framework.urls'), name = 'user-authentication'),
        path('api/isadmin/', AdminVewSet.as_view(), name = 'admin-view'),
        path('api/authenticate/', AuthenticatedViewSet.as_view(), name = 'auth-view'),
        path('api/Public/', PublicView.as_view(), name = 'public-view'),
        ]
