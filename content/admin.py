from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import TreeNode

admin.site.register(TreeNode, DraggableMPTTAdmin)
