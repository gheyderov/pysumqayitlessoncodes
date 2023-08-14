from django.contrib import admin
from accounts.models import User, BlockedIps

# Register your models here.

admin.site.register(User)

admin.site.register(BlockedIps)