from django.contrib import admin
from .models import Client, Category, Product, Sale, ProductCategory

# Register your models here.


class ProductCategoryAdminInline(admin.StackedInline):
    model = ProductCategory
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    #продуктите може да се додаваат и во делот за категории
    inlines = [ProductCategoryAdminInline, ]
    #категориите во листата се прикажуваат само нивните имиња
    list_display = ['name', ]

    #Не е дозволено бришење на категориите доколку корисникот не е супер корисник
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


class ProductAdmin(admin.ModelAdmin):
    exclude = ['user', ]

    #При креирањето на продуктот, корисникот се доделува автоматски според најавениот корисник
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(ProductAdmin, self).save_model(request, obj, form, change)

    #Откако еден продукт ќе биде дефиниран и зачуван, истиот може да се промени
    # само од корисникот кој го креирал продуктот
    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False

class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', ]

class ProductCategoryAdmin(admin.ModelAdmin):
    pass

class SaleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Sale, SaleAdmin)