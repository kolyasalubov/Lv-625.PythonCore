from django.contrib import admin
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from .models import *


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditor5Widget())

    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = PostAdminForm

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)