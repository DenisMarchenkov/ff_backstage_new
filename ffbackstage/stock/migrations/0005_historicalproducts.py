# Generated by Django 4.2.4 on 2023-11-02 11:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock', '0004_alter_brands_options_alter_products_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalProducts',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('code', models.IntegerField(db_index=True)),
                ('article', models.CharField(max_length=24)),
                ('name', models.CharField(max_length=255)),
                ('unit', models.CharField(blank=True, max_length=24)),
                ('description', models.TextField(blank=True)),
                ('initial_qua', models.IntegerField(default=0)),
                ('base_price', models.DecimalField(decimal_places=2, default=0, max_digits=11)),
                ('time_create', models.DateTimeField(blank=True, editable=False)),
                ('time_update', models.DateTimeField(blank=True, editable=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_supplied', models.BooleanField(default=True)),
                ('is_promo', models.BooleanField(default=False)),
                ('markup', models.DecimalField(decimal_places=5, default=1, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=5, default=1, max_digits=10)),
                ('slug', models.SlugField(max_length=255)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('author', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('brand', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='stock.brands')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Товар',
                'verbose_name_plural': 'historical Товары',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
