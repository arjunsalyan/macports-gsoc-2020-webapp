# Generated by Django 2.2.10 on 2020-05-01 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('port', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variant', models.CharField(default='', max_length=100)),
                ('port', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='port.Port')),
            ],
            options={
                'verbose_name': 'Variant',
                'verbose_name_plural': 'Variants',
                'db_table': 'variant',
            },
        ),
    ]
