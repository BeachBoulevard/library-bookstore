from django.contrib import admin

# Register your models here.
from .models import Author, Class, Book, BookInstance

class BookAdmin(admin.ModelAdmin):
  list_display = ("title", "author", "isbn", "assigned_class")

class AuthorAdmin(admin.ModelAdmin):
  list_display = ("first_name","last_name")

class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    
    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Class)
admin.site.register(BookInstance)