# Generated by Django 2.2.1 on 2019-08-31 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('principal', models.CharField(max_length=256)),
                ('location', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('age', models.PositiveIntegerField()),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='students', to='basic_app.School')),
            ],
        ),
    ]
