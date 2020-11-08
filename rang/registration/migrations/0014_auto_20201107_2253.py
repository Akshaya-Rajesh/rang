# Generated by Django 3.1.2 on 2020-11-07 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0013_auto_20201107_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='category',
            field=models.CharField(choices=[('senior', 'senior'), ('campus', 'campus'), ('school', 'school')], max_length=10),
        ),
        migrations.AlterField(
            model_name='participant',
            name='district',
            field=models.CharField(choices=[('thiruvananthapuram', 'Thiruvananthapuram'), ('wayanad', 'Wayanad'), ('ernakulam', 'Ernakulam'), ('idukki', 'Idukki'), ('malappuram', 'Malappuram'), ('kollam', 'Kollam'), ('kozhikode', 'Kozhikode'), ('kannur', 'Kannur'), ('palakkad', 'Palakkad'), ('thrissur', 'Thrissur'), ('pathanamthitta', 'Pathanamthitta'), ('alappuzha', 'Alappuzha'), ('kottayam', 'Kottayam'), ('kasaragod', 'Kasaragod')], max_length=20),
        ),
    ]
