# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import CustomUsers

# class CustomUserAdmin(UserAdmin):
#     model = CustomUsers
#     list_display = ['username', 'email', 'date_of_birth', 'is_staff']
#     fieldsets = UserAdmin.fieldsets + (
#         ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
#     )
#     add_fieldsets = UserAdmin.add_fieldsets + (
#         ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
#     )

# admin.site.register(CustomUsers, CustomUserAdmin)
