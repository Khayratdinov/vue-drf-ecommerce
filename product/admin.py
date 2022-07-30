from django.contrib import admin
# ============================================================================ #
from .models import Category, Product
# ============================================================================ #




# ================================= REGISTER ================================= #

admin.site.register(Category)
admin.site.register(Product)