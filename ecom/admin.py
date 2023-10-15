from django.contrib import admin
from .models import Customer, Product, Orders, Feedback


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):

    class Meta:
        verbose_name = "Ulanyjy"
        verbose_name_plural = "Ulanyjylar"


admin.site.register(Customer, CustomerAdmin)


class ProductAdmin(admin.ModelAdmin):

    class Meta:
        verbose_name = "Önüm"
        verbose_name_plural = "Önümler"


admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Orders, OrderAdmin)


class FeedbackAdmin(admin.ModelAdmin):

    class Meta:
        verbose_name = "Teswir"
        verbose_name_plural = "Teswirler"


admin.site.register(Feedback, FeedbackAdmin)
# Register your models here.
