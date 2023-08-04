```python
from django.contrib import admin
from .models import CrewMember, Cert, Qualification, Ship, Positions, Assignment, ShipCrewAllowance, shipschedule, port_details

# Register your models here.
admin.site.register(CrewMember)
admin.site.register(Cert)
admin.site.register(Qualification)
admin.site.register(Ship)
admin.site.register(Positions)
admin.site.register(Assignment)
admin.site.register(ShipCrewAllowance)
admin.site.register(shipschedule)
admin.site.register(port_details)
```