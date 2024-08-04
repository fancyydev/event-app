from django.contrib import admin
from .models import Country, State, Municipality

class StateInline(admin.TabularInline):
    model = State
    extra = 1

class MunicipalityInline(admin.TabularInline):
    model = Municipality
    extra = 1

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [StateInline]

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    list_filter = ('country',)
    inlines = [MunicipalityInline]

@admin.register(Municipality)
class MunicipalityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state')
    list_filter = ('state',)
