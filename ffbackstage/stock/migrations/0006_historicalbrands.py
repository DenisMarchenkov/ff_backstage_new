# Generated by Django 4.2.4 on 2023-11-02 12:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock', '0005_historicalproducts'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalBrands',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name_short', models.CharField(blank=True, max_length=24)),
                ('markup', models.DecimalField(decimal_places=5, default=1, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=5, default=1, max_digits=10)),
                ('vat', models.DecimalField(decimal_places=2, default=1, max_digits=3)),
                ('time_create', models.DateTimeField(blank=True, editable=False)),
                ('time_update', models.DateTimeField(blank=True, editable=False)),
                ('slug', models.SlugField(max_length=255)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Марка',
                'verbose_name_plural': 'historical Марки',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]