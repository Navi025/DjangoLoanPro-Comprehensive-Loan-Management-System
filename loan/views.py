from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.db.models import Q
from .models import Loan

# Create your views here.

class loanList(LoginRequiredMixin,ListView):
	template='loan/template_list'
	model=Loan

	def get_context_data(self, **kwargs):
		context = super(loanList, self).get_context_data(**kwargs)
		# Removed filter on non-existent 'is_staff' field
		context['loan_list']=Loan.objects.filter(person__company=self.request.user.person.company)
		return context

	