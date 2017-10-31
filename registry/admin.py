from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import RegHeaderImage, RegCategory, RegForm


class RegFormInline(admin.TabularInline):
	model = RegForm

class RegFormAdmin(admin.ModelAdmin):
	list_filter = ['updated', 'timestamp']
	readonly_fields = ['updated', 'timestamp']
	list_display = ("__str__", 'updated', 'timestamp')
	fields = ['title', 'slug', 'category', 'ext_link']
	search_fields = ['title']

	class Meta:
		model = RegForm


class RegCategoryAdmin(admin.ModelAdmin):
	inlines = [RegFormInline]
	class Meta:
		model = RegCategory


admin.site.register(RegHeaderImage)
admin.site.register(RegCategory, RegCategoryAdmin)
admin.site.register(RegForm, RegFormAdmin)