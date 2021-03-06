# Generated by Django 2.0.4 on 2018-04-08 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('castnautas', '0003_auto_20180408_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postagem',
            name='imagem_carrossel',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='postagem',
            name='imagem_grande',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='postagem',
            name='imagem_pequena',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='postagem',
            name='url_comentarios',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
    ]
