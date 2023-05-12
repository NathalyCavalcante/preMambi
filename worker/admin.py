from django.contrib import admin
from .models import Professions, Member # importação do model criando (.) pq é desse folder os models 

# Register your models here.

admin.site.register(Professions) # site do admin, registre Professions
admin.site.register(Member)