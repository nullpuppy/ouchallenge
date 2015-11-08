# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemSale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('list_price', models.IntegerField()),
                ('sell_price', models.IntegerField()),
                ('city', models.CharField(max_length=120)),
                ('cashless', models.BooleanField()),
            ],
        ),
    ]
