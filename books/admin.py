from django.contrib import admin
from .models import Book
import csv
from django.http import HttpResponse
# from import_export.admin import ImportExportModelAdmin

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
# class BookAdmin(ImportExportModelAdmin):
    list_display = ['name', 'pages', 'published_on']
    list_display_links = ['name']
    list_filter = ['genre']
    search_fields = [ 'name', ]
    actions = ['export_to_csv',]

    def export_to_csv(self, request, queryset):
        meta = self.model._meta
        print(meta.fields)
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={meta}.csv'
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])
        return response


