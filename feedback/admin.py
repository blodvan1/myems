from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Feedback
from .actions import mark_feedback_as_read
from .forms import FeedbackForm, FeedbackAddForm
#from django.db import models


class FeedbackAdmin(ModelAdmin):
	form = FeedbackForm
	search_fields = ('name', 'category', 'email', 'subject', 'emp_no')
	list_display = ('emp_no', 'name', 'category', 'email', 'subject', 'is_read' )
	list_editable = ('is_read',)
	#readonly_fields = ('created_on',)
	save_on_top = True
	actions_on_bottom = False
	actions = [mark_feedback_as_read]
	ordering = ('-created_on',)
	#formfield_overrides = {
		#models.CharField: {'widget': forms.TextInput(attrs={'size':'20'})},
		#models.TextField: {'widget': forms.Textarea(attrs={'rows': 4,'cols': 40})},
	#}

	def get_form(self, request, obj=None, **kwarg):

		if obj is None:
			return FeedbackAddForm
		else:
			return super(FeedbackAdmin, self).get_form(request, obj, **kwarg)

admin.site.register(Feedback, FeedbackAdmin)

