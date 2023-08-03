```python
from django import forms
from .models import CrewMember, Cert, Qualification, Ship, Positions, Assignment, ShipCrewAllowance, shipschedule, port_details

class CrewMemberForm(forms.ModelForm):
    class Meta:
        model = CrewMember
        fields = ['name', 'gender', 'contact', 'position', 'availability']

class CertForm(forms.ModelForm):
    class Meta:
        model = Cert
        fields = ['name', 'validity', 'expiry']

class QualificationForm(forms.ModelForm):
    class Meta:
        model = Qualification
        fields = ['crewmember', 'cert', 'expiry', 'date_issued']

class ShipForm(forms.ModelForm):
    class Meta:
        model = Ship
        fields = ['ship_name', 'ship_code', 'ship_brand']

class PositionsForm(forms.ModelForm):
    class Meta:
        model = Positions
        fields = ['position_name', 'position_code', 'contract_length', 'vacation_length']

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['Crewmember', 'ship_code', 'position']

class ShipCrewAllowanceForm(forms.ModelForm):
    class Meta:
        model = ShipCrewAllowance
        fields = ['ship_code', 'quantity_allocated', 'position']

class shipscheduleForm(forms.ModelForm):
    class Meta:
        model = shipschedule
        fields = ['ship_code', 'port_code', 'arrival_date', 'departure_date', 'port_type']

class port_detailsForm(forms.ModelForm):
    class Meta:
        model = port_details
        fields = ['port_name', 'port_code', 'port_country']
```