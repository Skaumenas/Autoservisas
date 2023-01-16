from django.contrib import admin
from .models import Automobilis, AutomobilisModelis, Paslauga, Uzsakymas, UzsakymoEilute


class UzsakymoEiluteInLine(admin.TabularInline):
    model = UzsakymoEilute
    readonly_fields = ("id",)
    can_delete = False
    extra = 0


class UzsakymasAdmin(admin.ModelAdmin):
    list_display = ("automobilis", "atsiemimo_data")
    inlines = [UzsakymoEiluteInLine]


class AutomobilisAdmin(admin.ModelAdmin):
    list_display = ("klientas", "vin_kodas", "valstybinis_nr", "automobilis_id")
    list_filter = ("klientas", "automobilis_id")
    search_fields = ("vin_kodas",)


class PaslaugaAdmin(admin.ModelAdmin):
    list_display = ("pavadinimas", "kaina")


admin.site.register(Automobilis, AutomobilisAdmin)
admin.site.register(AutomobilisModelis)
admin.site.register(Paslauga, PaslaugaAdmin)
admin.site.register(Uzsakymas, UzsakymasAdmin)
admin.site.register(UzsakymoEilute)
