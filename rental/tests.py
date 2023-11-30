import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from rental.models import Brand, Uav
from rental.forms import RenewUavForm

class BrandModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Brand.objects.create(brand_name='Lockheed')

    def test_brand_name_label(self):
        brand = Brand.objects.get(id=1)
        field_label = brand._meta.get_field('brand_name').verbose_name
        self.assertEqual(field_label, 'brand name')

    def test_brand_name_max_length(self):
        brand = Brand.objects.get(id=1)
        max_length = brand._meta.get_field('brand_name').max_length
        self.assertEqual(max_length, 100)

class RenewUavFormTest(TestCase):
    def test_renew_form_date_field_label(self):
        form = RenewUavForm()
        self.assertTrue(form.fields['renewal_date'].label is None or form.fields['renewal_date'].label == 'renewal date')

    def test_renew_form_date_field_help_text(self):
        form = RenewUavForm()
        self.assertEqual(form.fields['renewal_date'].help_text, 'Enter a future date.')

    def test_renew_form_date_in_past(self):
        date = datetime.date.today() - datetime.timedelta(days=1)
        form = RenewUavForm(data={'renewal_date': date})
        self.assertFalse(form.is_valid())

    def test_renew_form_date_today(self):
        date = datetime.date.today()
        form = RenewUavForm(data={'renewal_date': date})
        self.assertTrue(form.is_valid())

class UavListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_uavs = 10

        for uav_id in range(number_of_uavs):
            Uav.objects.create(
                model=f'tb {uav_id}',
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/rental/uavs/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_model(self):
        response = self.client.get(reverse('uavs'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('uavs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rental/uav_list.html')