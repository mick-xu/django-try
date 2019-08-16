from django.db import models
from django import forms
from datetime import datetime


# Create your models here.
class Navigation(models.Model):
    name = models.CharField("名称", max_length=16)
    parent = models.ForeignKey(
        'self', default=0, verbose_name='所属导航')
    # parent = models.IntegerField('所属导航', default=0)
    url = models.CharField("链接", max_length=128, blank=True, null=True)
    sort = models.IntegerField("排序")

    class Meta:
        verbose_name = '网站导航'
        verbose_name_plural = '网站导航'
        db_table = 'app_navigation'
        ordering = ('-sort', )

    def __str__(self):
        return self.name


class Article(models.Model):
    navigation = models.ForeignKey(Navigation, default=0, verbose_name='导航')
    title = models.CharField("标题", max_length=128, help_text='输入文章标题')
    keyword = models.CharField(
        "关键词",
        max_length=128,
        blank=True,
        null=True,
        help_text='关键词，用于 SEO，不超过 64 个汉字')
    description = models.CharField(
        "描述",
        max_length=256,
        blank=True,
        null=True,
        help_text='描述，用于 SEO，不超过 128 个汉字')
    contents = models.TextField("内容", max_length=None)
    author = models.CharField(
        "作者", max_length=16, blank=True, null=True, help_text='输入作者名字')
    is_slide = models.BooleanField('幻灯片', default=False)
    is_top = models.BooleanField('置顶', default=False)
    pub_date = models.DateTimeField("发布日期", editable=False, auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = u'文章资讯'
        ordering = ('-pub_date', )

    def __str__(self):
        return self.title


class Case(models.Model):
    navigation = models.ForeignKey(Navigation, default=0, verbose_name='导航')
    title = models.CharField('名称', max_length=64, help_text="请输入案例名称")
    cover = models.ImageField('图标', max_length=128)
    keyword = models.CharField(
        "关键词",
        max_length=128,
        blank=True,
        null=True,
        help_text='关键词，用于 SEO，不超过 64 个汉字')
    description = models.CharField(
        "描述",
        max_length=256,
        blank=True,
        null=True,
        help_text='描述，用于 SEO，不超过 128 个汉字')
    contents = models.TextField("内容", max_length=None)
    pub_date = models.DateTimeField('发布时间', editable=False, auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = u'客户案例'
        ordering = ('-pub_date', )

    def __str__(self):
        return self.title

    # def __unicode__(self):
    #     return self.title


class SiteInfo(models.Model):
    site_name = models.CharField('网站名称', max_length=64)
    domain = models.CharField("网站域名", max_length=128, blank=True, null=True)
    keyword = models.CharField(
        '关键词', max_length=128, blank=True, null=True, help_text='网站 SEO 关键词')
    description = models.CharField(
        '网站描述', max_length=256, blank=True, null=True, help_text='网站 SEO 描述信息')
    site_mobile = models.CharField(
        '企业电话', max_length=11, blank=True, null=True)
    site_mail = models.EmailField(
        '企业邮箱', max_length=128, blank=True, null=True)
    admin_mobile = models.CharField(
        '站长手机', max_length=11, blank=True, null=True)
    admin_mail = models.EmailField(
        '站长邮箱', max_length=128, blank=True, null=True)

    class Meta:
        verbose_name = '站点信息'
        verbose_name_plural = '站点信息'

    def __str__(self):
        return self.site_name


class Slide(models.Model):
    title = models.CharField("标题", max_length=128)
    desc = models.CharField("描述", max_length=256, blank=True, null=True)
    cover = models.ImageField('图片', max_length=128)
    url = models.CharField("链接", max_length=128, blank=True, null=True)

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = "轮播图"

    def __str__(self):
        return self.title


class FriendlyLink(models.Model):
    name = models.CharField("名称", max_length=16)
    cover = models.ImageField(
        verbose_name="图片",
        max_length=128,
        upload_to='%Y%m',
        blank=True,
        null=True)
    url = models.CharField("链接", max_length=128, blank=True, null=True)
    sort = models.IntegerField("排序", auto_created=True)

    class Meta:
        verbose_name = "友情链接"
        verbose_name_plural = "友情链接"

    def __str__(self):
        return self.name
