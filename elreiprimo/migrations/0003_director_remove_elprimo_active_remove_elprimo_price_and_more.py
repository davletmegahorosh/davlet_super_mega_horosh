# Generated by Django 4.1.7 on 2023-02-16 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elreiprimo', '0002_rename_elreiprimo_elprimo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='elprimo',
            name='active',
        ),
        migrations.RemoveField(
            model_name='elprimo',
            name='price',
        ),
        migrations.RemoveField(
            model_name='elprimo',
            name='quantity',
        ),
        migrations.AddField(
            model_name='elprimo',
            name='duration',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elreiprimo.elprimo')),
            ],
        ),
        migrations.AddField(
            model_name='elprimo',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elreiprimo.director'),
        ),
    ]