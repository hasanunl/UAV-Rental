# Generated by Django 4.2.7 on 2023-11-29 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0003_uavinstance_renter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uavinstance',
            options={'ordering': ['return_date'], 'permissions': (('can_mark_returned', 'Set UAV as returned'),)},
        ),
    ]
