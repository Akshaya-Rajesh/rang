# Generated by Django 3.1.2 on 2020-11-07 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0012_auto_20201107_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='category',
            field=models.CharField(choices=[('campus', 'campus'), ('senior', 'senior'), ('school', 'school')], max_length=10),
        ),
        migrations.AlterField(
            model_name='participant',
            name='district',
            field=models.CharField(choices=[('kasaragod', 'Kasaragod'), ('kozhikode', 'Kozhikode'), ('pathanamthitta', 'Pathanamthitta'), ('ernakulam', 'Ernakulam'), ('thiruvananthapuram', 'Thiruvananthapuram'), ('kottayam', 'Kottayam'), ('alappuzha', 'Alappuzha'), ('idukki', 'Idukki'), ('palakkad', 'Palakkad'), ('kollam', 'Kollam'), ('wayanad', 'Wayanad'), ('malappuram', 'Malappuram'), ('thrissur', 'Thrissur'), ('kannur', 'Kannur')], max_length=20),
        ),
    ]