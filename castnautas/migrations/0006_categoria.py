# Generated by Django 2.0.4 on 2018-04-08 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('castnautas', '0005_auto_20180408_1738'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postagens', models.ManyToManyField(to='castnautas.Postagem')),
            ],
        ),
    ]
