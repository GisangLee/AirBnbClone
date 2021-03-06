from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.RoomType, models.Facility, models.HouseRule, models.Amenity)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "used_by",
    )

    def used_by(self, obj):
        return obj.rooms.count()


class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price", "city",)},
        ),
        (
            "Times",
            {"fields": ("check_in", "check_out", "instant_book")}
        ),
        (
            "Spaces",
            {"fields": ("guests", "beds", "bedrooms", "baths")}
        ),
        (
            "More About Spaces",
            {"fields": ("amenities", "facilities", "houserules")}
        ),
        (
            "Last Details",
            {"fields": ("host", "room_type",)}
        )
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "baths",
        "bedrooms",
        "address",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "photo_count",
        "total_rating",
    )

    ordering = ("name", "price", "bedrooms")

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "houserules",
        "city",
        "country",
    )

    raw_id_fields = (
        "host",
    )

    search_fields = ["^city", "^host__username"]

    filter_horizontal = (
        "amenities",
        "facilities",
        "houserules",
    )

    def count_amenities(self, obj):
        return obj.amenities.count()

    def photo_count(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "get_thumbnail",
    )

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="70px" src="{obj.file.url}"/>')

    get_thumbnail.short_description = "Thumbnail"
