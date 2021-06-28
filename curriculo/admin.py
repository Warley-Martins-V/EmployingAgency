from django.contrib import admin
from .models import *

class LinguagensDominadasInline(admin.TabularInline):
    model = LinguagensDominadas
    extra = 1


class DataBaseDominadasInline(admin.TabularInline):
    model = DataBaseDominadas
    extra = 1


class FrameworkDominadosInline(admin.TabularInline):
    model = FrameworkDominados
    extra = 1


class CurriculoAdmin(admin.ModelAdmin):
    inlines = [
        LinguagensDominadasInline,
        DataBaseDominadasInline,
        FrameworkDominadosInline,
    ]


admin.site.register(Curriculo, CurriculoAdmin)

admin.site.register(ExperienciaProfissional)

