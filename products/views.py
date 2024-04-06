from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import Product, Order
from django.urls import reverse_lazy
from django.db.models import Q # for search method
from django.http import JsonResponse
from .forms import ContactForm, CheckoutForm
from django.http import JsonResponse
from django.contrib.auth.views import PasswordChangeView
import json
from django.views.decorators.csrf import csrf_exempt  




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

# class ProductCheckoutView(LoginRequiredMixin, DetailView):
#     model = Product
#     template_name = 'checkout.html'
#     login_url     = 'login'


# def paymentComplete(request):
#     if request.method == 'POST':
#         # Process payment details here
#         # Retrieve card details from request.POST['card_number'], request.POST['expiry_date'], request.POST['cvv']
#         # Perform payment processing logic here
#         # For demonstration purposes, let's assume payment is successful
#         # You should replace this with your actual payment processing logic
#         # Example:
#         card_number = request.POST.get('card_number')
#         expiry_date = request.POST.get('expiry_date')
#         cvv = request.POST.get('cvv')
#         # Process payment...
#         return JsonResponse('Payment completed!', safe=False)
#     else:
#         return JsonResponse('Invalid request!', status=400)
     
@csrf_exempt
def paymentComplete(request):
    # Simply redirect to the list page
    return redirect('list')
     
class ProductCheckoutView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'checkout.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['checkout_form'] = CheckoutForm()  
        return context

    def post(self, request, *args, **kwargs):
        form = CheckoutForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Payment completed successfully!')
            return redirect('list')
        else:
            return self.render_to_response(self.get_context_data(form=form))
     

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

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
