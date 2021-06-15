from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.views.generic.base import View
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings
from django.contrib import messages


from dashboard.forms import MessageForm
from dashboard.models import *
from dashboard.mixines import *

from .mixin import *

# Create your views here.


class HomeTemplateView(BaseMixin,TemplateView):
    template_name = 'home/base/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.filter(deleted_at__isnull=True)
        context['service'] = service.objects.filter(deleted_at__isnull=True)
        context['brand'] = Brands.objects.filter(deleted_at__isnull=True)
        context['trend_products'] = Products.objects.filter(
            deleted_at__isnull=True).order_by('-view_count')
        context['brand'] = Brands.objects.filter(deleted_at__isnull=True)
        
        return context

# products view


class ProductListView(BaseMixin, NonDeletedItemMixin, ListView):
    template_name = 'home/product/list.html'
    model = Products


class ProductDetailView(DetailView):
    template_name = 'home/product/detail.html'
    model = Products
    context_object_name = 'product_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        p_slug = self.kwargs.get('slug')
        obj = Products.objects.get(pk=p_slug)
        category = obj.categories
        context['similar_product'] = Products.objects.filter(
            categories__name=category).exclude(slug=p_slug)
        return context

# about

class AboutListView(BaseMixin, NonDeletedItemMixin, ListView):
    model = Abouts
    template_name = 'home/about/about.html'
    
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['about'] = Abouts.objects.filter(deleted_at__isnull=True)
       context['testimonial'] = Testimonials.objects.filter(deleted_at__isnull=True)
       context['service'] = service.objects.filter(deleted_at__isnull=True)
       context['blog'] = Blog.objects.filter(deleted_at__isnull=True)
       context['brand'] = Brands.objects.filter(deleted_at__isnull=True)

       return context

# contact

class ContactView(CreateView):
    template_name = 'home/contact/contact.html'
    form_class = MessageForm
    success_url = reverse_lazy('contact')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contact.objects.filter(deleted_at__isnull=True)
        form = MessageForm(self.request.POST or None)
        context['form'] = MessageForm()

        return context

    def post(self, request, *args, **kwargs):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('first_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        obj = Message.objects.create(
            first_name=first_name, last_name=last_name, email=email, phone=phone, message=message)
        return redirect('contact')

    def form_valid(self, form):
        email = form.cleaned_data['email']

        if "@" not in email:
            return render(self.request, self.template_name,
                          {
                              'error': 'Invalid email',
                              'form': form
                          })
        else:
            pass
        return super().form_valid(form)

# newsletter

class SubscriptionView(View):
    def post(self, request, *args, **kwargs):
        email = self.request.POST.get('email')
        if Subscription.objects.filter(email=email).exists():
            messages.warning(request, "Wow, Already Subscribed.")
        else:
            obj = Subscription.objects.create(email=email)
            messages.success(
                request, f'Thank you for Subscription {email}')
            subject = "Thank you for joining Us"
            from_email = settings.EMAIL_HOST_USER
            to_email = [email]
            html_template = get_template(
                "home/newsletter/newsletter.html").render()
            plain_text = get_template(
                "home/newsletter/newsletter.txt").render()
            message = EmailMultiAlternatives(
                subject, plain_text, from_email, to_email)

            message.attach_alternative(html_template, "text/html")
            message.send()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


