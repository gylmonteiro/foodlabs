# Generated by Django 4.0.6 on 2022-07-30 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('addresses', '0002_alter_address_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='users.user'),
        ),
    ]
