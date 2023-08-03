```python
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='CrewMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=10)),
                ('contact', models.CharField(max_length=200)),
                ('availability', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Positions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_name', models.CharField(max_length=200)),
                ('position_code', models.CharField(max_length=200)),
                ('contract_length', models.IntegerField()),
                ('vacation_length', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='CrewMember',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Positions'),
        ),
        migrations.CreateModel(
            name='Cert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('validity', models.IntegerField()),
                ('expiry', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiry', models.DateField()),
                ('date_issued', models.DateField()),
                ('cert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Cert')),
                ('crewmember', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.CrewMember')),
            ],
        ),
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ship_name', models.CharField(max_length=200)),
                ('ship_code', models.CharField(max_length=200)),
                ('ship_brand', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crewmember', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.CrewMember')),
                ('ship_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Ship')),
            ],
        ),
        migrations.CreateModel(
            name='ShipCrewAllowance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_allocated', models.IntegerField()),
                ('ship_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Ship')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Positions')),
            ],
        ),
        migrations.CreateModel(
            name='shipschedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival_date', models.DateField()),
                ('departure_date', models.DateField()),
                ('port_type', models.CharField(max_length=200)),
                ('ship_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Ship')),
            ],
        ),
        migrations.CreateModel(
            name='port_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port_name', models.CharField(max_length=200)),
                ('port_code', models.CharField(max_length=200)),
                ('port_country', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='shipschedule',
            name='port_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.port_details'),
        ),
    ]
```