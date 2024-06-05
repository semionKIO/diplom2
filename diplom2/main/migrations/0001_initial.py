# Generated by Django 5.0.3 on 2024-05-10 10:55

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Имя')),
                ('text', models.TextField(verbose_name='Отзыв')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации')),
                ('estimation', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10)], verbose_name='Оценка')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
