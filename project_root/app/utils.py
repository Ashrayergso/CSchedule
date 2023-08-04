```python
from django.db.models import Q
from .models import CrewMember, Ship, Assignment, Positions

def assignCrewToShips():
    # Fetch all crew members and ships
    crew_members = CrewMember.objects.all()
    ships = Ship.objects.all()

    # Iterate over each ship
    for ship in ships:
        # Fetch the positions required for this ship
        positions_required = ship.shipcrewallowance_set.all()

        # Iterate over each position
        for position in positions_required:
            # Fetch crew members who are available and have the required position
            available_crew = crew_members.filter(Q(position=position.position) & Q(availibility=True))

            # If there are no available crew members for this position, continue to the next position
            if not available_crew.exists():
                continue

            # Assign the first available crew member to this ship and position
            crew_member = available_crew.first()
            assignment = Assignment.objects.create(Crewmember=crew_member, ship_code=ship, position=crew_member.position)

            # Set the crew member's availability to False
            crew_member.availibility = False
            crew_member.save()

    return "ASSIGNMENT_SUCCESS"
```