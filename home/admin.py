from django.contrib import admin

# Register your models here.
from .models import User, Expense, Balance

class ExpenseInline(admin.TabularInline):
	model = Expense
	extra = 1

class BalanceInline(admin.StackedInline):
	model = Balance

class UserAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields' : ['firstname']}),
		(None, {'fields' : ['lastname']})
	]
	inlines = [BalanceInline, ExpenseInline]

admin.site.register(User, UserAdmin)
