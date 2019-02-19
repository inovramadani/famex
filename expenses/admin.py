from django.contrib import admin

# Register your models here.
from .models import User, Expense

class ExpenseInline(admin.TabularInline):
	model = Expense
	extra = 1

class UserAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields' : ['firstname']}),
		(None, {'fields' : ['lastname']})
	]
	inlines = [ExpenseInline]

admin.site.register(User, UserAdmin)
