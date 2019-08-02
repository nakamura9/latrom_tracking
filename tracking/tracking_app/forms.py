from django import forms
from tracking_app.models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (HTML, 
                                 Layout, 
                                 Row, 
                                 Column,
                                 Submit)


class CustomerForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = Customer
        widgets = {
            'roles': forms.RadioSelect
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name_of_customer',
            Row(
                Column('login_account', css_class='col-6'),
                Column('password', css_class='col-6'),
                ),
            'roles',
            Row(
                Column('contacts', css_class='col-6'),
                Column('phone', css_class='col-6'),
                ),
            'address',
            'parent_customer',
        )

        self.helper.add_input(Submit('submit', 'Submit'))



class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = Customer
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name_of_customer',
            Row(
                Column('login_account', css_class='col-6'),
                Column('password', css_class='col-6'),
                ),
            HTML('Role: {{object.role_string}}</p>'),
            Row(
                Column('contacts', css_class='col-6'),
                Column('phone', css_class='col-6'),
                ),
            'address',
        )

        self.helper.add_input(Submit('submit', 'Submit'))



class DeviceCreateForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = Device
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'customer',
            Row(
                Column('id_number', 
                        'type',
                        'target_name',
                        'sim_card_no',
                        'license_plate_no',
                        'contacts_no',
                        css_class='col-6'),
                Column('expired_date',
                        'filter_lbs',
                        'overspeed_km_hr',
                        'phone_no',
                        'fuel_per_100km',
                         css_class='col-6'),
                ),
            'icon',
            'remark'
            
        )

        self.helper.add_input(Submit('submit', 'Submit'))


class DeviceUpdateForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = Device
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name_of_customer',
            Row(
                Column('id_number', 
                        'type',
                        'target_name',
                        'sim_card_no',
                        'license_plate_no',
                        'contacts_no',
                        css_class='col-6'),
                Column('expired_date',
                        'filter_lbs',
                        'overspeed_km_hr',
                        'phone_no',
                        'fuel_per_100km',
                         css_class='col-6'),
                ),
            'icon',
            'remark'
            
        )

        self.helper.add_input(Submit('submit', 'Submit'))


class ReportForm(forms.Form):
    from_ = forms.DateField()
    to = forms.DateField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('from_', css_class='col-5'),
                Column('to', css_class='col-5'),
                Column(Submit('submit', 'Search'), css_class='col-2'),
            )
        )