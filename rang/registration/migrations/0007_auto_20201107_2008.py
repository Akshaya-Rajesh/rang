# Generated by Django 3.1.2 on 2020-11-07 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_auto_20201107_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='category',
            field=models.CharField(choices=[('senior', 'senior'), ('school', 'school'), ('campus', 'campus')], max_length=10),
        ),
        migrations.AlterField(
            model_name='participant',
            name='district',
            field=models.CharField(choices=[('kannur', 'Kannur'), ('thiruvananthapuram', 'Thiruvananthapuram'), ('kollam', 'Kollam'), ('malappuram', 'Malappuram'), ('idukki', 'Idukki'), ('palakkad', 'Palakkad'), ('alappuzha', 'Alappuzha'), ('thrissur', 'Thrissur'), ('wayanad', 'Wayanad'), ('pathanamthitta', 'Pathanamthitta'), ('kottayam', 'Kottayam'), ('kozhikode', 'Kozhikode'), ('kasaragod', 'Kasaragod'), ('ernakulam', 'Ernakulam')], max_length=20),
        ),
    ]
