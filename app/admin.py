from django.db import models
from django.contrib import admin
from .models import SiteInfo, Navigation, Article, Case, Slide, FriendlyLink
from django import forms

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'navigation', 'keyword', 'description', 'author', 'pub_date')
    list_filter = ['pub_date']
    date_hierarchy = 'pub_date'
    search_fields = ['title']
    description = '新闻文章'
    formfield_overrides = {
        # models.CharField: {
        #     'widget': forms.Textarea
        # },
        # models.TextField: {
        #     'contents': RichTextEditorWidget
        # },
    }

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(ArticleAdmin, self).formfield_for_dbfield(
            db_field, **kwargs)
        if db_field.name == 'description':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield


admin.site.register(Article, ArticleAdmin)


class CaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    list_filter = ['pub_date']
    date_hierarchy = 'pub_date'
    description = '客户案例'

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(CaseAdmin, self).formfield_for_dbfield(
            db_field, **kwargs)
        if db_field.name == 'description':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield


admin.site.register(Case, CaseAdmin)


class SiteInfoAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'domain', 'site_mobile')


admin.site.register(SiteInfo, SiteInfoAdmin)


class NavigationAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'sort')
    search_fields = ['name']


admin.site.register(Navigation, NavigationAdmin)


class SlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'cover', 'url')


admin.site.register(Slide, SlideAdmin)


class FriendlyLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'sort')


admin.site.register(FriendlyLink, FriendlyLinkAdmin)
