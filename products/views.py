from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from cart.forms import CartAddProductForm
from products.models import Category, Product, ProductLike, Rating


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'range': range(5)
    }
    return render(request, 'product/list.html', context)


def search_product(request, category_slug=None):
    search_term = request.GET.get('search', '')

    products = Product.objects.filter(name__icontains=search_term, available=True)

    context = {
        'search': search_term,
        'products': products
    }
    return render(request, 'product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    product.total_views += 1
    product.save()
    related_items = Product.objects.filter(parent=product)
    context = {
        'product': product, 'related_items': related_items, 'cart_product_form': CartAddProductForm(), 'range': range(5)
    }
    return render(request, 'product/detail.html', context)


@login_required
def product_like(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    user = request.user
    ProductLike.objects.get_or_create(product=product, user=user)
    product.save()
    return redirect(product.get_absolute_url())


@login_required
def product_rate(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)

    comment = request.POST.get('comment', '')
    rating = request.POST.get('rating', 0)
    if product:
        if not Rating.objects.filter(user=request.user, product=product, rate_type=Rating.RATE).exists():
            Rating.objects.create(user=request.user, product=product, message=comment, rate=rating)
        else:
            Rating.objects.create(user=request.user, product=product, message=comment, rate=rating,
                                  rate_type=Rating.COMMENT)

        return redirect(product.get_absolute_url())
        # ProductLike.objects.get_or_create(product=product, user=user)
        # product.save()
        # return redirect(product.get_absolute_url())

        #
        # class ProductRateView(LoginRequiredMixin, TemplateView):
        #     template_name = 'products/product_details.html'
        #
        #     def post(self, request, *args, **kwargs):
        #         slug = kwargs.get('slug', None)
        #         comment = request.POST.get('comment', '')
        #         rating = request.POST.get('rating', 0)
        #         product = Product.objects.filter(slug=slug).first()
        #         if product:
        #             if not Rating.objects.filter(user=self.request.user, product=product, rate_type=Rating.RATE).exists():
        #                 Rating.objects.create(user=self.request.user, product=product, message=comment, rate=rating)
        #             else:
        #                 Rating.objects.create(user=self.request.user, product=product, message=comment, rate=rating,
        #                                       rate_type=Rating.COMMENT)
        #
        #         return redirect(reverse('product_detail', args=[slug]))
