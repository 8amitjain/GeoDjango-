from django import forms

from .models import Person, Position, SalesDeed, FMW, SalesDeedRepresentative, GiftDeed, GiftDonorDeed, PurchaseDeed,\
                    Deed


class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.fields['position'].queryset = Position.objects.none()

            if 'gender' in self.data:
                try:
                    gender_id = int(self.data.get('gender'))
                    self.fields['position'].queryset = Position.objects.filter(gender_id=gender_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['position'].queryset = self.instance.gender.position_set.order_by('name')

        except AttributeError:
            pass


class SalesDeedForm(forms.ModelForm):
    class Meta:
        model = SalesDeed
        fields = '__all__'
        exclude = ('unique_id', 'seller')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.fields['fwm'].queryset = FMW.objects.none()

            if 'gender' in self.data:
                try:
                    gender_id = int(self.data.get('gender'))
                    self.fields['fwm'].queryset = FMW.objects.filter(gender_id=gender_id)
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['fwm'].queryset = self.instance.gender.fwm_set

        except AttributeError:
            pass


class SalesDeedRepresentativeForm(forms.ModelForm):
    class Meta:
        model = SalesDeedRepresentative
        fields = '__all__'
        exclude = ('representative_unique_id', 'representative_seller')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.fields['representative_fwm'].queryset = FMW.objects.none()
            print(self.data, 'data')

            if 'representative_gender' in self.data:
                try:
                    gender_id = int(self.data.get('representative_gender'))
                    self.fields['representative_fwm'].queryset = FMW.objects.filter(gender_id=gender_id)
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['representative_fwm'].queryset = self.instance.representative_gender.fwm_set

        except AttributeError:
            pass


class GiftDeedForm(forms.ModelForm):
    class Meta:
        model = GiftDeed
        fields = '__all__'
        exclude = ('unique_id', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.fields['fwm'].queryset = FMW.objects.none()

            if 'gender' in self.data:
                try:
                    gender_id = int(self.data.get('gender'))
                    self.fields['fwm'].queryset = FMW.objects.filter(gender_id=gender_id)
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['fwm'].queryset = self.instance.gender.fwm_set

        except AttributeError:
            pass


class GiftDonorDeedForm(forms.ModelForm):
    class Meta:
        model = GiftDonorDeed
        fields = '__all__'
        exclude = ('representative_unique_id', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.fields['representative_fwm'].queryset = FMW.objects.none()
            print(self.data, 'data')

            if 'representative_gender' in self.data:
                try:
                    gender_id = int(self.data.get('representative_gender'))
                    self.fields['representative_fwm'].queryset = FMW.objects.filter(gender_id=gender_id)
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['representative_fwm'].queryset = self.instance.representative_gender.fwm_set

        except AttributeError:
            pass


class PurchaseDeedForm(forms.ModelForm):
    class Meta:
        model = PurchaseDeed
        fields = '__all__'
        exclude = ('unique_id', )


class DeedEditDownloadForm(forms.ModelForm):
    class Meta:
        model = Deed
        fields = '__all__'
        exclude = ('name', )
