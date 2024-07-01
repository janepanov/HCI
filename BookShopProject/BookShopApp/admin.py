from django.contrib import admin
from .models import Book, Author, BookAuthor
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    exclude = ('user', )

    def has_add_permission(self, request):
        return request.user.is_superuser

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(AuthorAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        author = Author.objects.get(user=request.user)
        return queryset.filter(bookauthor__author=author, bookauthor__book__description__isnull=False).distinct()


class BookAdmin(admin.ModelAdmin):
    search_fields = ('description', )

    def has_add_permission(self, request):
        return Author.objects.filter(user=request.user).exists()

    def has_change_permission(self, request, obj=None):
        if obj is not None:
            return BookAuthor.objects.filter(book=obj, author__user=request.user).exists()
        return False

class BookAuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(BookAuthor, BookAuthorAdmin)