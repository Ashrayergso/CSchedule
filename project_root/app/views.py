```python
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CrewMember, Cert, Qualification, Ship, Positions, Assignment, ShipCrewAllowance, shipschedule, port_details
from .forms import CrewMemberForm, CertForm, QualificationForm, ShipForm, PositionsForm, AssignmentForm, ShipCrewAllowanceForm, shipscheduleForm, port_detailsForm

def home(request):
    return render(request, 'app/home.html')

def crew_member_list(request):
    crew_members = CrewMember.objects.all()
    return render(request, 'app/crew_member_list.html', {'crew_members': crew_members})

def ship_list(request):
    ships = Ship.objects.all()
    return render(request, 'app/ship_list.html', {'ships': ships})

def assignment_list(request):
    assignments = Assignment.objects.all()
    return render(request, 'app/assignment_list.html', {'assignments': assignments})

def create_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'ASSIGNMENT_SUCCESS')
            return redirect('assignment_list')
    else:
        form = AssignmentForm()
    return render(request, 'app/create_assignment.html', {'form': form})

def edit_assignment(request, pk):
    assignment = Assignment.objects.get(pk=pk)
    if request.method == 'POST':
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            messages.success(request, 'ASSIGNMENT_SUCCESS')
            return redirect('assignment_list')
    else:
        form = AssignmentForm(instance=assignment)
    return render(request, 'app/edit_assignment.html', {'form': form})

def assign_crew_to_ships(request):
    # TODO: Implement the logic for automatic crew-to-ship assignment
    pass
```