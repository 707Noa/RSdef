# Generated by Django 5.1 on 2024-09-08 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0003_grupo_publicaciongrupo_comentariogrupo'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='foto_perfil',
            field=models.ImageField(blank=True, null=True, upload_to='grupo_perfiles/'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='portada',
            field=models.ImageField(blank=True, null=True, upload_to='grupo_portadas/'),
        ),
    ]
