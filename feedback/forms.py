from django import forms
from .models import Feedback
from myems.models import Employee

class FeedbackAddForm(forms.ModelForm):

	email = forms.CharField(widget = forms.TextInput(attrs = {'size': 20}))
	comment = forms.CharField(widget = forms.Textarea(attrs = {'rows': 6, 'cols': 60, 'style': 'resize:none;' }))
	
	#check if emp_no is found in database
	def clean_emp_no(self):
		print(self.cleaned_data)
		emp_no = self.cleaned_data.get('emp_no')
		if emp_no and not Employee.objects.filter(pk = emp_no).exists():
			raise forms.ValidationError("Invalid employee Number")

		return self.cleaned_data.get('emp_no')

	#multi field validation
	def clean(self):
		formData = super(FeedbackAddForm, self).clean()
		category = formData.get('category')
		comment = formData.get('comment')
		if category == '5' and comment:
			if 'reference_no=' not in comment:
					self.add_error("comment", "Your complaint should have tag reference_no=")
		return formData


	class Meta:
		model = Feedback
		fields = ('emp_no', 'name', 'subject', 'category', 'email','comment' , 'is_read', )


class FeedbackForm(forms.ModelForm):

	comment = forms.CharField(widget = forms.Textarea(attrs = {'rows': 6, 'cols': 60, 'style': 'resize:none;' }))
	created_on = forms.CharField(widget = forms.TextInput(attrs = {'readonly': 'readonly','size': '38'}))

	class Meta:
		model = Feedback
		fields = '__all__'