# Generated by Django 4.0.4 on 2022-05-11 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SzczegolyRefundacji',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identyfikator_leku', models.TextField(blank=True, null=True)),
                ('zakres_wskazan', models.TextField(blank=True, null=True)),
                ('zakres_wskazan_pozarejestracyjnych', models.TextField(blank=True, null=True)),
                ('poziom_odplatnosci', models.TextField(blank=True, null=True)),
                ('wysokosc_doplaty', models.DecimalField(decimal_places=2, max_digits=7, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa_leku', models.TextField()),
                ('substancja_czynna', models.TextField()),
                ('postac', models.TextField()),
                ('dawka_leku', models.TextField()),
                ('zawartosc_opakowania', models.TextField()),
                ('identyfikator_leku', models.TextField()),
                ('refundacje', models.ManyToManyField(to='DrugSearch.szczegolyrefundacji')),
            ],
        ),
    ]
