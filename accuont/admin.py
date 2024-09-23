# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ["full_name", "phone", "is_admin",]
#
#     readonly_fields = ["password", "last_login"]


from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import AdminPasswordChangeForm

from .models import User
from .forms import UserChangeForm


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    change_password_form = AdminPasswordChangeForm  # فرم تغییر پسورد
    readonly_fields = ["date_joined"]
    list_display = ('full_name', "phone", 'is_admin')
    list_filter = ('is_admin', 'is_active')
    fieldsets = (
        (None, {'fields': ('full_name', 'user_name', 'phone', 'password')}),
        ('Personal info', {'fields': ('date_of_birth', "adress", "national_code", "date_joined")}),
        ('Permissions', {'fields': ('is_admin', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('full_name', "user_name", 'phone', 'password1', 'password2'),
        }),
    )
    search_fields = ('user_name',)
    filter_horizontal = ()
    ordering = ('date_joined',)
    
    # اضافه کردن قابلیت تغییر پسورد
    # def get_urls(self):
    #     from django.urls import path
    #     return [
    #         path(
    #             '<id>/password/',
    #             self.admin_site.admin_view(self.change_password),
    #             name='auth_user_password_change',
    #         ),
    #     ] + super().get_urls()

    def change_password(self, request, id):
        return self.changeform_view(request, id, form_url='password/')


admin.site.register(User, UserAdmin)
