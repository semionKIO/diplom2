# Generated by Django 5.0.3 on 2024-05-13 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Название услуги')),
                ('text', models.TextField(verbose_name='Описание услуги')),
                ('car', models.ImageField(upload_to='images/')),
                ('prise', models.TextField(verbose_name='Стоимость')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
    ]
