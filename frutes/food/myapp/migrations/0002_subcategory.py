# Generated by Django 3.2.8 on 2022-02-28 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mcate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.maincategory')),
            ],
        ),
    ]
