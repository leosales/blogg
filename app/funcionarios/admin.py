from django.contrib import admin

# default: "Administração do Django"
admin.site.site_header= 'Painel de Controle'
# default: "Administração do Site"
admin.site.index_title = 'Recursos'
# default: ”Site de administração do Django"
admin.site.site_title = 'Funcionarios'

# Register your models here.
from .models import Funcionario
from .models import Cargo

admin.site.register(Funcionario)
admin.site.register(Cargo)