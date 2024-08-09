import os
import django
from django.db.models import Q, Count, F, When, Case, Value, BooleanField

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here

from main_app.models import Profile, Order, Product

# Create queries within functions


def get_profiles(search_string=None) -> str:
    if search_string is None:
        return ""

    query = Q(full_name__icontains=search_string) | Q(email__icontains=search_string) | Q(phone_number__icontains=search_string)
    found_profiles = Profile.objects.annotate(num_orders=Count('order')).filter(query).order_by("full_name")

    return "\n".join(
        f"Profile: {p.full_name}, email: {p.email}, phone number: {p.phone_number}, orders: {p.num_orders}"
        for p in found_profiles) if found_profiles else ""


def get_loyal_profiles() -> str:
    found_profiles = Profile.objects.get_regular_customers()
    return "\n".join(f"Profile: {p.full_name}, orders: {p.num_orders}" for p in found_profiles) if found_profiles else ""


def get_last_sold_products() -> str:
    latest_order = Order.objects.order_by('-creation_date').first()
    if not latest_order or not latest_order.products.all():
        return ""
    sold_products = latest_order.products.order_by('name')
    return f"Last sold products: {', '.join(p.name for p in sold_products)}"


def get_top_products() -> str:
    most_sold_products = Product.objects.annotate(num_orders=Count('order')).order_by('-num_orders', "name")[:5]

    if not most_sold_products:
        return ""

    top_products = '\n'.join(f"{p.name}, sold {p.num_orders} times" for p in most_sold_products if p.num_orders != 0)

    return f"Top products:\n{top_products}" if top_products else ""


def apply_discounts() -> str:
    updated_orders = Order.objects.annotate(
        num_products=Count('products')
    ).filter(
        is_completed=False,
        num_products__gt=2
    ).update(
        total_price=F('total_price') * 0.9
    )

    return f"Discount applied to {updated_orders} orders."


def complete_order() -> str:
    oldest_order = Order.objects.prefetch_related('products').filter(is_completed=False).order_by('creation_date').first()

    if not oldest_order:
        return ""

    for product in oldest_order.products.all():
        if product.in_stock == 1:
            product.is_available = False
        product.in_stock -= 1
        product.save()
    oldest_order.is_completed = True

    # oldest_order.products.update(
    #     in_stock=F('in_stock') - 1,
    #     is_available=Case(
    #         When(in_stock=1, then=Value(False)),
    #         default=F('is_available'),
    #         output_type=BooleanField()
    #     )
    # )

    oldest_order.save()

    return "Order has been completed!"
