from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.




class CustomUserAdmin(UserAdmin):
    model = User
    list_display = [
        'username',
          'email', ''
          'is_staff',
          'is_active',
          "is_superuser"
          ]
    list_filter = [
        'is_staff',
        'is_active'
        ]
    search_fields = (
        'username',
        'email'
        )
    ordering = ('email',)
    fieldsets = (
        ("authentication", {
            'fields':(
                'username',
                'email',
                'password'
                )
            }),
        ('Permissions',{
            'fields':(
                'is_staff',
                'is_active',
                'is_superuser'
                )
            }),
           ( "group permissions",{
                'fields':(
                    "groups",
                    "user_permissions"
                    )
            }),
            ("importent dates",{
                'fields':(
                    "last_login",
                )
            })
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                        'username',
                        'email',
                        'password1',
                        'password2',
                        'is_staff',
                        'is_active'
                           )}
        ),
    )

admin.site.register(User, CustomUserAdmin)
