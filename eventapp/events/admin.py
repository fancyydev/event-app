from django.contrib import admin
from .models import Event, Activity, Schedule, Room, Sponsor, Images
from django.http import HttpResponse
from accounts.utils import generate_excel_report, generate_pdf_report
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ['id','name_event', 'initial_date', 'end_date', 'program', 'is_active']
    list_filter = ['initial_date', 'end_date']
    search_fields = ['name_event', 'description']
    actions = ['download_excel_report', 'download_pdf_report']

    def download_excel_report(self, request, queryset):
        # Asumimos que solo un evento está seleccionado a la vez
        if queryset.count() == 1:
            event = queryset.first()
            buffer = generate_excel_report(event)

            # Preparar la respuesta HTTP con el archivo Excel
            response = HttpResponse(
                buffer, 
                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )
            response['Content-Disposition'] = f'attachment; filename="reporte_usuarios_{event.id}.xlsx"'
            return response
        else:
            self.message_user(request, "Por favor, selecciona un solo evento para generar el reporte.", level='warning')
    
    def download_pdf_report(self, request, queryset):
        if queryset.count() == 1:
            event = queryset.first()
            pdf = generate_pdf_report(event)

            # Preparar la respuesta HTTP con el archivo PDF
            response = HttpResponse(
                pdf, 
                content_type='application/pdf'
            )
            response['Content-Disposition'] = f'attachment; filename="reporte_usuarios_{event.id}.pdf"'
            return response
        else:
            self.message_user(request, "Por favor, selecciona un solo evento para generar el reporte.", level='warning')

    download_excel_report.short_description = "Descargar reporte en Excel"
    download_pdf_report.short_description = "Descargar reporte en PDF"

class RoomAdmin(admin.ModelAdmin):
    list_display = ('id','name_room',)

class ActivityAdmin(admin.ModelAdmin):
    list_display = ['id', 'title_activity', 'description', 'author', 'event', 'room', 'start_datetime']
    list_filter = ['start_datetime', 'event']
    search_fields = ['title_activity', 'description', 'event']
    prepopulated_fields = {'slug': ('title_activity',)}

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'activity', 'created_at']
    list_filter = ['user', 'activity', 'created_at']
    search_fields = ['user', 'activity']


class SponsorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'link', 'tier']
    list_filter = ['name', 'link']
    search_fields = ['name', 'link']
    
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'event'] 
    list_filter = ['event']   
    search_fields = ['id', 'event']

    
# Register the models in the desired order
admin.site.register(Event, EventAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Images, ImagesAdmin)


