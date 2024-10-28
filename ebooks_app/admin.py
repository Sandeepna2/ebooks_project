from django.contrib import admin
from .models import Book, BookAuthor,BookCategory

# Register your models here.
class BookInline(admin.TabularInline):
        model = Book
        extra = 1


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    raw_id_fields = ('author','category')
    
    list_display = ['id', 'title', 'author', 'price', 'published_date', 'status','category']
    list_filter = ('status', 'published_date')
    search_fields = ('title', 'author')
    list_per_page = 20
    date_hierarchy = 'published_date'
    ordering = ('-published_date',)
    prepopulated_fields = {'slug': ('title',)}
    
    
    
@admin.register(BookAuthor)
class BookAuthorAdmin(admin.ModelAdmin):
    
    list_display = ['name','user', 'bio', 'website' , 'profile_picture']
    list_filter = ('user',)
    search_fields = ('user', 'bio')
    list_per_page = 20
    ordering = ('user',)
    # prepopulated_fields = {'slug': ('user',)}
    
@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):

    list_display = ['id', 'name']
    list_filter = ('name',)
    search_fields = ('name', 'description')
    list_per_page = 20
    ordering = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = [BookInline]
    
    



