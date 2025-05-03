from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # matches /accounts/****
    path('accounts/', include('accounts.urls')),
    
    # matches /dashboard/****
    path('dashboard/', include('dashboard.urls')),

    # matches /asset/****
    path('asset/', include('assetmanager.urls')),

    # matches /loans/****
    path('loans/', include('loan.urls')),

    # Redirect /user-guide/ to dashboard user-guide view
    path('user-guide/', RedirectView.as_view(url='/dashboard/user-guide/', permanent=False)),
]
