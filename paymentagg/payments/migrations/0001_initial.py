# Generated by Django 2.1.5 on 2019-02-02 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('middle_name', models.CharField(blank=True, max_length=250, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('external_id', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'patients',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('amount', models.DecimalField(decimal_places=3, max_digits=9)),
                ('external_id', models.CharField(max_length=250)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='payments.Patient')),
            ],
            options={
                'db_table': 'payments',
            },
        ),
    ]
