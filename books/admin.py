from django.contrib import admin
from books.models import Book, Editor

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'asin', 'site')
    list_filter = ('site','editor',)
    search_fields = ('title',)
    
admin.site.register(Book, BookAdmin)

class EditorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    
admin.site.register(Editor, EditorAdmin)