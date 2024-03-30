from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import Product, Order
from django.urls import reverse_lazy
from django.db.models import Q # for search method
from django.http import JsonResponse
from .forms import ContactForm
from django.http import JsonResponse
from django.contrib.auth.views import PasswordChangeView
import json




class ProductListView(ListView):
    model = Product
    template_name = 'list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'detail.html'


class SearchResultsListView(ListView):
	model = Product
	template_name = 'search_results.html'

	def get_queryset(self): # new
		query = self.request.GET.get('q')
		return Product.objects.filter(
		Q(title__icontains=query) | Q(designer_name__icontains=query)
		)

class ProductCheckoutView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'checkout.html'
    login_url     = 'login'


def paymentComplete(request):
	body = json.loads(request.body)
	print('BODY:', body)
	product = Product.objects.get(id=body['productId'])
	Order.objects.create(
		product=product
	)
	return JsonResponse('Payment completed!', safe=False)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
     
            # Perform any additional processing (e.g., send email)
            # Return a JSON response indicating success
            #return JsonResponse({'success': True})
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('list')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
     success_url = reverse_lazy('list')  # Redirect to the list page after changing password

     def form_valid(self, form):
        response = super().form_valid(form)
        # Additional actions after changing password
        return response
