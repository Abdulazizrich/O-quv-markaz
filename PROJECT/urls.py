from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('', admin.site.urls),
    path('bosh/', bosh_sahifa),
    path('yonalish/', yonalish),
    path('xona/', xona),
    path('ustoz/', ustoz),
    path('guruh/', guruh),
    path('oquvchi/', oquvchi),
    path('tolov/', tolov),
    path('yonalish/<int:id>/tahrirlash/', yonalish_tahrirlash),
    path('xona/<int:id>/tahrirlash/', xona_tahrirlash),
    path('ustoz/<int:id>/tahrirlash/', ustoz_tahrirlash),
    path('guruh/<int:id>/tahrirlash/', guruh_tahrirlash),
    path('oquvchi/<int:id>/tahrirlash/', oquvchi_tahrirlash),
    path('tolov/<int:id>/tahrirlash/', tolov_tahrirlash),
    path('yonalish/<int:id>/ochir/',yonalish_ochir),
    path('xona/<int:id>/ochir/',xona_ochir),
    path('ustoz/<int:id>/ochir/',ustoz_ochir),
    path('guruh/<int:id>/ochir/',guruh_ochir),
    path('oquvchi/<int:id>/ochir/',oquvchi_ochir),
    path('tolov/<int:id>/ochir/',tolov_ochir),
]
