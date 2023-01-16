# Generated by Django 4.1.1 on 2023-01-16 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteka', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='automobilismodelis',
            options={'verbose_name': 'Modelis', 'verbose_name_plural': 'Modeliai'},
        ),
        migrations.AddField(
            model_name='uzsakymoeilute',
            name='status',
            field=models.CharField(blank=True, choices=[('a', 'Administruojama'), ('t', 'tvarkoma'), ('b', 'baigta'), ('p', 'pasiimti'), ('d', 'atiduota')], default='a', help_text='Status', max_length=1),
        ),
        migrations.AlterField(
            model_name='uzsakymoeilute',
            name='kiekis',
            field=models.IntegerField(help_text='Įveskite paslaugų kiekį.', verbose_name='Kiekis'),
        ),
    ]