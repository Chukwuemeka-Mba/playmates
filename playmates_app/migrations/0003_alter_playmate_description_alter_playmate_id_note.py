# Generated by Django 4.0.3 on 2022-03-21 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('playmates_app', '0002_playmate_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playmate',
            name='description',
            field=models.TextField(default='Hiking, dinner date?'),
        ),
        migrations.AlterField(
            model_name='playmate',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('note', models.TextField(default='Write a note here')),
                ('playmate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playmates_app.playmate')),
            ],
        ),
    ]
