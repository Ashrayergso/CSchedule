```python
from django.test import TestCase
from .models import CrewMember, Cert, Qualification, Ship, Positions, Assignment, ShipCrewAllowance, shipschedule, port_details
from .utils import assignCrewToShips

class CrewMemberModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CrewMember.objects.create(name='John Doe', gender='M', contact='1234567890', availibility=True)

    def test_name_label(self):
        crewmember = CrewMember.objects.get(id=1)
        field_label = crewmember._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    # Add more tests for other fields and models

class AssignCrewToShipsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create some test data for crew members, ships, and assignments

    def test_assign_crew_to_ships(self):
        # Call the assignCrewToShips function
        assignCrewToShips()
        # Check the assignments are as expected

    # Add more tests for other functions and views
```