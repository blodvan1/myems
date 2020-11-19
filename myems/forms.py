from django import forms
from .models import Employee, Salary, Dg
from django.utils import timezone
from django.utils.safestring import mark_safe

class AdminImageFieldWidget(forms.widgets.FileInput):
	def __init__(self, placeholder='/images/profile/placeholder.thumbnail.jpg'):
		self.placeholder = placeholder
		super(AdminImageFieldWidget, self).__init__({})

	#def render(self, name, image, attrs=None):
		#render_html = '<img src="%s"/>' % (image.thumbnail.url) if image and hasattr(image, "url") else '<img src="%s"/>' % (self.placeholder)
		#return mark_safe("%s%s" % (render_html, super(AdminImageFieldWidget, self).render(name,image,attrs)))
class DgForm(forms.ModelForm):
	
	class Meta:
		model = Dg
		fields = ('id', 'commercial_designation_in_english', 'code_ean13', 'commercial_reference', 'un_code')


class EmployeeForm(forms.ModelForm):
	
# Its important when you use SelectDateWidget to specify the year as it will only show

	# Future years from today not past

	hire_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
	
	#birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(1980, 2025)), initial=timezone.now)
	birth_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

	image = forms.ImageField(label='Profile Image', widget=AdminImageFieldWidget(), required=False)


	class Meta:
		model = Employee
		fields = ('image', 'emp_no', 'birth_date', 'first_name', 'last_name', 'gender', 'hire_date','ib_admin','ib_unstuffing','ib_putaway')


class SalaryForm(forms.ModelForm):

	class Meta:
		model = Salary
		fields = '__all__'


class DgSearchForm(forms.Form):
	search_text = forms.CharField(
					required = False,
					label='Search UN Code using EAN',
					widget=forms.TextInput(attrs={'placeholder': 'Scan Barcode'})
                  )