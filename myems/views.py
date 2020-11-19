from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404 , redirect
from .forms import EmployeeForm, DgForm
from .models import Employee, Salary, generate_next_emp_no, Dg, generate_next_id_no
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView, RedirectView
from django.urls import reverse_lazy

from .forms import DgSearchForm
from search_views.search import SearchListView
from search_views.filters import BaseFilter

def my_profile(request, pk):
	profile = get_object_or_404(Employee, pk=pk)

	if request.method.upper() == 'POST':
		form = EmployeeForm(request.POST, instance=profile)
		if form.is_valid(): 
			# <process form cleaned data>
			form.save()
			return redirect('my_profile', pk=pk)

	form = EmployeeForm(instance=profile)
	return render(request, 'profile.html', {'form': form})
	#return HttpResponse("<h1>This is my first function based view %s </h1>" % pk)

#function based view
def index(request):
	if request.method.upper() == 'GET':
		return render(request, 'index.html', {})


#class based view
class IndexView(View):

	def get(self, request, *args, **kwargs):
		return render(request, 'index.html', {})


	def post(self, request, *args, **kwargs):
		return render(request, 'index.html', {})

#generic class view, easiest
class IndexGenericView(TemplateView):
	template_name = 'index.html'

class ProfileView(View):

	form_class = EmployeeForm
	#initial = {'hire_date': 'TODAY_DATE'}
	template_name = 'my_profile_detail.html'

	def get(self, request, *args, **kwargs):
		form = self.form_class(instance = self.get_context_data().get('profile'))
		return render(request, self.get_template_name(), {'form': form})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST, instance = self.get_object())
		if form.is_valid():
			#<process form cleaned data>
			form.save()
			return HttpResponseRedirect('/success/')
		return render(request, self.template_name, {'form': form})

	def get_template_name(self):
		"""Returns the name of the template we should render"""
		return self.template_name

	def get_context_data(self):
		"""Returns the data passed to the template"""

		return {
			'profile': self.get_object(),
		}

	def get_object(self):
		"""Returns the BlogPost instance that the view displays"""
		return get_object_or_404(Employee, pk = self.kwargs.get('pk'))


class ProfileListView(ListView):
	model = Employee
	template_name = 'profile_list.html'
	paginate_by = 100

	def get_queryset(self):
		order_by_field = self.request.GET.get('order_by') or '-hire_date'
		queryset = super(ProfileListView, self).get_queryset()
		return queryset.order_by(order_by_field)

class ProfileDetailView(DetailView):
	template_name = 'my_profile_detail.html'
	model = Employee

	def get_context_data(self, **kwargs):
		context = super(ProfileDetailView, self).get_context_data(**kwargs)
		context['salary_entries'] = Salary.objects.filter(emp_no__exact=self.object.emp_no)
		return context

class ProfileCreateView(CreateView):
	template_name = 'my_profile_create.html'
	form_class = EmployeeForm
	success_url = reverse_lazy('profile_list')

	def get_initial(self):
		initial = super(ProfileCreateView, self).get_initial()
		initial['emp_no'] = generate_next_emp_no()
		return initial

class ProfileDeleteView(DeleteView):
	model = Employee
	success_url = reverse_lazy('profile_list')

	def get(self, request, *args, **kwargs):
		"""
		Take note this is a hack as we dont want to show confirmation page before deleting, by default 
		djamgo will try to look for a template called objectname__confirm_delete.html
		"""
		return self.post(request, *args, **kwargs)


class ProfileUpdateView(UpdateView):
	template_name = 'my_profile_update.html'
	model = Employee
	form_class = EmployeeForm
	success_url = reverse_lazy('profile_list')

class DgCreateView(CreateView):
	template_name = 'dg_create.html'
	form_class = DgForm
	success_url = reverse_lazy('dg')

	def get_initial(self):
		initial = super(DgCreateView, self).get_initial()
		initial['id'] = generate_next_id_no()
		return initial


class DgFilter(BaseFilter):
	search_fields = {
	'search_text': ['code_ean13']

	}

class DgSearchList(SearchListView):
    model = Dg
    paginate_by = 100
    template_name = "dg.html"
    form_class = DgSearchForm
    filter_class = DgFilter