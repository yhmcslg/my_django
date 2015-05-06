from django.contrib import admin
from models import Post,Category

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ('id','title','author','content','pub_data')


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id','name',)


admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
