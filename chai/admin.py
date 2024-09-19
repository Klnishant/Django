from django.contrib import admin
from .models import ChaiCertificate, ChaiVariety, Stores, chaiReview

# Register your models here.

class ChaiReviewInline(admin.TabularInline):
    model = chaiReview
    extra = 1

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name','type','date_added')
    inlines = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name','location')
    filter_horizontal = ('chai_variety',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai','certificate_number','issued_date','valid_till')

admin.site.register(ChaiVariety,ChaiVarietyAdmin)
admin.site.register(Stores,StoreAdmin)
admin.site.register(ChaiCertificate,ChaiCertificateAdmin)
