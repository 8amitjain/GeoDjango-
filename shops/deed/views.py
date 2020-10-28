from django.shortcuts import render, redirect, get_object_or_404
from uuid import uuid4
from datetime import datetime

from .forms import PersonCreationForm, SalesDeedForm, SalesDeedRepresentativeForm, GiftDeedForm, GiftDonorDeedForm, \
                   PurchaseDeedForm, DeedEditDownloadForm
from .models import Person, Position, SalesDeed, FMW, SalesDeedRepresentative, GiftDeed, GiftDonorDeed, PurchaseDeed

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa


class Render:
    @staticmethod
    def render(path: str, params: dict):
        template = get_template('deed/sales_deed_download_form.html')
        html = template.render(params)
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            return HttpResponse(response.getvalue(), content_type='application/pdf')
        else:
            return HttpResponse("Error Rendering PDF", status=400)


class Render1:
    @staticmethod
    def render(path: str, params: dict):
        template = get_template('deed/gift_deed_download_form.html')
        html = template.render(params)
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            return HttpResponse(response.getvalue(), content_type='application/pdf')
        else:
            return HttpResponse("Error Rendering PDF", status=400)


class Render2:
    @staticmethod
    def render(path: str, params: dict):
        template = get_template('deed/purchase_deed_download_form.html')
        html = template.render(params)
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            return HttpResponse(response.getvalue(), content_type='application/pdf')
        else:
            return HttpResponse("Error Rendering PDF", status=400)


def select_deed(request):
    return render(request, 'deed/select_deed.html', )


def sales_deed(request):
    form = SalesDeedForm()
    form2 = SalesDeedRepresentativeForm()
    if request.method == 'POST':
        form = SalesDeedForm(request.POST)
        form2 = SalesDeedRepresentativeForm(request.POST)
        if form.is_valid() and form2.is_valid():
            unique_id = str(uuid4())
            formm = form.save(commit=False)
            formm.unique_id = unique_id
            formm.save()

            formm2 = form2.save(commit=False)
            formm2.representative_unique_id = unique_id
            formm2.save()
            return redirect('form-download-sales', unique_id=unique_id)
    return render(request, 'deed/sales_deed.html', {'form': form, 'form2': form2})


def load_fwm(request):
    gender_id = request.GET.get('gender_id')
    fwm = FMW.objects.filter(gender_id=gender_id)
    return render(request, 'deed/fwm_dropdown_list_options.html', {'fwm': fwm})


def load_fwm2(request):
    gender_id = request.GET.get('gender_id2')
    fwm = FMW.objects.filter(gender_id=gender_id)
    return render(request, 'deed/fwm_dropdown_list_options2.html', {'fwm': fwm})


def gift_deed(request):
    form = GiftDeedForm()
    form2 = GiftDonorDeedForm()
    if request.method == 'POST':
        form = GiftDeedForm(request.POST)
        form2 = GiftDonorDeedForm(request.POST)
        if form.is_valid() and form2.is_valid():
            unique_id = str(uuid4())
            formm = form.save(commit=False)
            formm.unique_id = unique_id
            formm.save()

            formm2 = form2.save(commit=False)
            formm2.representative_unique_id = unique_id
            formm2.save()
            return redirect('form-download-gift', unique_id=unique_id)
    return render(request, 'deed/gift_deed.html', {'form': form, 'form2': form2})


def load_gift(request):
    gender_id = request.GET.get('gender_id')
    fwm = FMW.objects.filter(gender_id=gender_id)
    return render(request, 'deed/gift_dropdown_list_options.html', {'fwm': fwm})


def load_gift2(request):
    gender_id = request.GET.get('gender_id2')
    fwm = FMW.objects.filter(gender_id=gender_id)
    return render(request, 'deed/gift_dropdown_list_options2.html', {'fwm': fwm})


def purchase_deed(request):
    form = PurchaseDeedForm()
    if request.method == 'POST':
        form = PurchaseDeedForm(request.POST)
        if form.is_valid():
            unique_id = str(uuid4())
            formm = form.save(commit=False)
            formm.unique_id = unique_id
            formm.save()
            return redirect('form-download-purchase', unique_id=unique_id)
    return render(request, 'deed/purchase_deed.html', {'form': form})


def download_form_purchase(request, unique_id):
    sale_deed = PurchaseDeed.objects.get(unique_id=unique_id)
    now = datetime.now()  # current date and time
    year = now.strftime("%Y")
    month = now.strftime("%b")
    day = now.strftime("%d")
    context = {
        'deed': sale_deed,
        'year': year,
        'month': month,
        'day': day,
    }
    return Render2.render('deed/purchase_deed_download_form.html', context)


def download_form_sales(request, unique_id):
    sale_deed = SalesDeed.objects.get(unique_id=unique_id)
    sales_deed_representative = SalesDeedRepresentative.objects.get(representative_unique_id=unique_id)

    now = datetime.now()  # current date and time
    year = now.strftime("%Y")
    month = now.strftime("%b")
    day = now.strftime("%d")

    sale_deed_age = int(year) - int(sale_deed.birth_date.strftime("%Y"))
    sales_deed_representative_age = int(year) - int(sales_deed_representative.representative_birth_date.strftime("%Y"))
    context = {
        'sale_deed': sale_deed,
        'sale_deed_age': sale_deed_age,
        'sales_deed_representative': sales_deed_representative,
        'sales_deed_representative_age': sales_deed_representative_age,
        'year': year,
        'month': month,
        'day': day,
    }
    # form = DeedEditDownloadForm()
    # if request.method == 'POST':
    #     form = DeedEditDownloadForm(request.POST)
    #     if form.is_valid():
    #         formm = form.save(commit=False)
    #         formm.name = 'sales_deed'
    #         formm.save()
    return Render.render('deed/sales_deed_download_form.html', context)


def download_form_gift(request, unique_id):
    sale_deed = GiftDeed.objects.get(unique_id=unique_id)
    sales_deed_representative = GiftDonorDeed.objects.get(representative_unique_id=unique_id)

    now = datetime.now()  # current date and time
    year = now.strftime("%Y")
    month = now.strftime("%b")
    day = now.strftime("%d")

    sale_deed_age = int(year) - int(sale_deed.birth_date.strftime("%Y"))
    sales_deed_representative_age = int(year) - int(sales_deed_representative.representative_birth_date.strftime("%Y"))
    context = {
        'sale_deed': sale_deed,
        'sale_deed_age': sale_deed_age,
        'sales_deed_representative': sales_deed_representative,
        'sales_deed_representative_age': sales_deed_representative_age,
        'year': year,
        'month': month,
        'day': day,
    }
    return Render1.render('deed/gift_deed_download_form.html', context)

#
# def deed_edit_download(request):
#     form = DeedEditDownloadForm()
#     if request.method == 'POST':
#         form = DeedEditDownloadForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('select-deed')
#     return render(request, 'deed/form1.html', {'form': form})


def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_add')
    return render(request, 'deed/form1.html', {'form': form})


def person_create_view2(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_add')
    return render(request, 'deed/form2.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'deed/form1.html', {'form': form})


# AJAX
def load_cities(request):
    country_id = request.GET.get('gender_id')
    cities = Position.objects.filter(gender_id=country_id).all()
    return render(request, 'deed/city_dropdown_list_options.html', {'cities': cities})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)


def load_income(request):
    position_id = request.GET.get('position_id')
    pos = Position.objects.get(id=position_id)
    if pos.earning == "YES":
        data = 'show'
        return render(request, 'deed/income_dropdown_list_options.html', {'data': data})
    else:
        data = 'hide'
        return render(request, 'deed/income_dropdown_list_options.html', {'data': data})

