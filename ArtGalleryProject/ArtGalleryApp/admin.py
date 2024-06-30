import datetime

from django.contrib import admin
from .models import ArtPiece, Artist, ArtExhibition

# Register your models here.


class ArtExhibitionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser


class ArtistAdmin(admin.ModelAdmin):
    exclude = ['user', ]

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        if request.user.is_superuser:
            future_exhibitions = ArtExhibition.objects.filter(from_date__gte=datetime.date.today()).all()

            return obj in future_exhibitions

        else:
            filtered_exhibitions = ArtExhibition.objects.filter(artpiece__artist=request.user.artist).distinct()

            return obj in filtered_exhibitions

    def save_model(self, request, obj, form, change):
        obj.user = request.user

        super().save_model(request, obj, form, change)

class ArtPieceAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            if hasattr(request.user, 'artist'):
                obj.artist = request.user.artist

        super().save_model(request, obj, form, change)

    def has_add_permission(self, request):
        return request.user.is_superuser or hasattr(request.user, 'artist')

    def has_change_permission(self, request, obj=None):
        if obj is not None and not request.user.is_superuser:
            return obj.artist == request.user.artist

        return super().has_change_permission(request, obj)


admin.site.register(ArtPiece, ArtPieceAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(ArtExhibition, ArtExhibitionAdmin)