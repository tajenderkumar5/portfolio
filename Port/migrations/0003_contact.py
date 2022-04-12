# Generated by Django 3.2 on 2021-10-02 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Port', '0002_delete_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=255)),
                ('UserEmail', models.CharField(max_length=50)),
                ('Subject', models.CharField(max_length=255)),
                ('Message', models.TextField()),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]