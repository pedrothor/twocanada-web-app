# Generated by Django 4.2.6 on 2023-10-31 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twocanadaapp', '0002_parceiros'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sobre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('imagem', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'sobre',
                'verbose_name_plural': 'sobre',
                'db_table': 'sobre',
            },
        ),
        migrations.AlterField(
            model_name='parceiros',
            name='imagem',
            field=models.CharField(max_length=300),
        ),
    ]
