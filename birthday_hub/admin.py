from django.contrib import admin

from .models import Birthday, User

# Configurations for models in admin interface


class BirthdayAdmin(admin.ModelAdmin):
    date_hierarchy = "birthdate"
    list_display = ["id", "first_name", "last_name", "nickname", "birthdate"]
    list_filter = ["birthdate"]
    search_fields = ["first_name", "last_name", "nickname"]


class UserAdmin(admin.ModelAdmin):
    date_hierarchy = "birthdate"
    list_display = ["id", "first_name", "last_name", "email", "birthdate"]
    list_filter = ["birthdate"]
    search_fields = ["email", "first_name", "last_name", "nickname"]


admin.site.register(Birthday, BirthdayAdmin)
admin.site.register(User, UserAdmin)
