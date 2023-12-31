# Generated by Django 4.2.4 on 2023-10-23 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('sessions', models.PositiveSmallIntegerField(choices=[(1, '12 sessions in month'), (2, '16 sessions in month'), (3, '30 sessions in month')], default=1, null=True)),
                ('membership_date', models.DateField(null=True)),
                ('GYM', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
