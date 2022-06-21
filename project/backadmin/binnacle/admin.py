from django.contrib import admin
from .models import Area, Post, Tipo

# Register your models here.

class AreaAdmin(admin.ModelAdmin):
    #define que campos son estaticos y no se pueden modificar en el panel
    #de admon
    readonly_fields = ('created', 'updated')

class TipoAdmin(admin.ModelAdmin):
    #define que campos son estaticos y no se pueden modificar en el panel
    #de admon
    readonly_fields = ('created', 'updated')


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    #Se agrega para decirle al motor administrador de django
    # que muestre mas columnas
    
    list_display = ('inventario', 'serie', 'falla', 'post_areas')
    
    #Para ordenamientos, si es solo un elemento como TUPLA
    #TUPLA -> ordering = ('author',)
    ordering = ('author', 'published')

    #formulario de busqueda
    #author no, debe llevar __username
    searchfields = ('inventario', 'serie', 'author__username', 'area__name')

    # Para una busqueda por años gerarquia en la parte superior
    date_hierarchy = 'published'

    # Da un cuadro del lado derecho para filtros
    list_filter = ('author__username', 'area__name',)

    #Todo esto para mandar llamar las categorias dentro del list_display
    #Categorias es un dato complejo por lo que no se puede mostrar tal cual
    # se tiene que hacer un recorrido para listarlo

    def post_areas(self, obj):
        #return "ALGO"
        return ", ".join( [c.name for c in obj.area.all().order_by("name")] )
    #Esto le cambia el nombre a post_categories
    post_areas.short_description = 'Areas'

# Para administrar este modelo desde el panel admin
admin.site.register(Area, AreaAdmin)
admin.site.register(Tipo, TipoAdmin)
admin.site.register(Post, PostAdmin)