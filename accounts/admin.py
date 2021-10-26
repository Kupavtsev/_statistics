from django.contrib import admin

# Register your models here.
# from django.contrib.auth.admin  import UserAdmin
from .models                    import Account

# Register your models here.

class AccountAdmin( admin.ModelAdmin ):
    list_display        = ( 'username', 'email', 'last_login', 'date_joined' )
    list_display_links  = ( 'username', 'email', 'date_joined' )
    search_fields       = ( 'username', 'email' )


admin.site.register( Account, AccountAdmin )