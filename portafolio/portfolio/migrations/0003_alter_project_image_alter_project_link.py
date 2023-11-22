# Generated by Django 4.2.7 on 2023-11-19 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_project_options_remove_project_titulo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to=' Project', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.URLField(blank='True', null='True', verbose_name='Enlace'),
        ),
    ]