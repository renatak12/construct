from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UsuarioCreationForm, UsuarioChangeForm
from .models import Usuario


@admin.register(Usuario)
class UsuarioUsersAdmin(UserAdmin):
    form = UsuarioChangeForm
    add_form = UsuarioCreationForm
    model = Usuario
    list_display = [
    "email",
    "username",
    "cargo",
    "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("cargo",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("cargo",)}),)
