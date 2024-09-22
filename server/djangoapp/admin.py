from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

# CarModelInline class
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1  # Optionally, allow adding one extra CarModel instance by default

# CarModelAdmin class

class CarModelAdmin(admin.ModelAdmin):
    inlines = [CarModelInline] 
# CarMakeAdmin class with CarModelInline

# CarMakeAdmin class with CarModelInline
@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('car_make_id', 'name', 'description')
    search_fields = ('name', 'description')

# Register models here
admin.site.register(CarMake)
admin.site.register(CarModel)