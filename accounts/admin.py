from django.contrib import admin
from .models import (
    UserAccount,
    Profile,
    Friendship
)

admin.site.register(UserAccount)
admin.site.register(Profile)
admin.site.register(Friendship)