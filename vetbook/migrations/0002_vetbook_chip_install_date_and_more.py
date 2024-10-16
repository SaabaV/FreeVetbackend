# Generated by Django 5.1.1 on 2024-10-16 10:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vetbook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vetbook',
            name='chip_install_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vetbook',
            name='chip_install_location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='vetbook',
            name='chip_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='vetbook',
            name='clinic',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='vetbook',
            name='registration_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='ClinicalExamination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examination_date', models.DateField()),
                ('results', models.TextField(blank=True, null=True)),
                ('clinic', models.CharField(blank=True, max_length=255, null=True)),
                ('vetbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='examinations', to='vetbook.vetbook')),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treatment_type', models.CharField(choices=[('deworming', 'Дегельминтизация'), ('ectoparasites', 'Обработка от эктопаразитов')], max_length=255)),
                ('medication_name', models.CharField(max_length=255)),
                ('treatment_date', models.DateField()),
                ('vetbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='treatments', to='vetbook.vetbook')),
            ],
        ),
        migrations.CreateModel(
            name='Vaccination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('batch_number', models.CharField(blank=True, max_length=50, null=True)),
                ('expiration_date', models.DateField(blank=True, null=True)),
                ('administration_date', models.DateField(blank=True, null=True)),
                ('validity_date', models.DateField(blank=True, null=True)),
                ('vetbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vaccinations', to='vetbook.vetbook')),
            ],
        ),
    ]
