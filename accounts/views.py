from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from blogs.models import Post
from products.models import Product, Category
from cart.forms import CartAddProductForm

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class HomeView(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        kwargs['blogs'] = Post.objects.filter(is_active=True).order_by('-id')[:3]
        kwargs['products'] = Product.objects.filter(product_type=Product.PRODUCT)[:10]
        kwargs['range'] = range(5)
        kwargs['cart_product_form'] = CartAddProductForm()
        return kwargs
