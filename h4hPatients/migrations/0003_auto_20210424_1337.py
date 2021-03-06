# Generated by Django 3.1.7 on 2021-04-24 13:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('h4hPatients', '0002_auto_20210423_1418'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=64, primary_key=True, serialize=False)),
                ('role', models.CharField(max_length=256)),
                ('firstname', models.CharField(max_length=256)),
                ('lastnames', models.CharField(max_length=256)),
                ('id_number', models.CharField(max_length=128)),
                ('dateOfBirth', models.DateField()),
                ('contactNumber', models.CharField(max_length=128, null=True)),
                ('email', models.CharField(max_length=128, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('deletedOn', models.DateTimeField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='dateOfBirth',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='deletedOn',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Theatre',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=64, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=1024)),
                ('hospitalWing', models.CharField(max_length=256)),
                ('Category', models.CharField(max_length=256)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('deletedOn', models.DateTimeField(null=True)),
                ('createdBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='h4hPatients.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=64, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256, null=True)),
                ('description', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('deletedOn', models.DateTimeField(null=True)),
                ('createdBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='h4hPatients.staff')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='h4hPatients.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=64, primary_key=True, serialize=False)),
                ('foreignKeyType', models.CharField(max_length=256)),
                ('foreignKey', models.CharField(max_length=256)),
                ('shortText', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=1024)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('deletedOn', models.DateTimeField(null=True)),
                ('createdBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='h4hPatients.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=64, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=1024)),
                ('hospitalWing', models.CharField(max_length=256)),
                ('Category', models.CharField(max_length=256)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('deletedOn', models.DateTimeField(null=True)),
                ('createdBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='h4hPatients.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=64, primary_key=True, serialize=False)),
                ('foreignKeyType', models.CharField(max_length=256)),
                ('foreignKey', models.CharField(max_length=256)),
                ('startTime', models.DateTimeField(null=True)),
                ('endTime', models.DateTimeField(null=True)),
                ('comments', models.TextField()),
                ('cancellationReason', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('deletedOn', models.DateTimeField(null=True)),
                ('createdBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='h4hPatients.staff')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='createdBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='h4hPatients.staff'),
        ),
    ]
