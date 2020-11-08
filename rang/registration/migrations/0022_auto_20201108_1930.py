# Generated by Django 3.1.2 on 2020-11-08 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0021_auto_20201108_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paricipation',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.event'),
        ),
        migrations.AlterField(
            model_name='paricipation',
            name='participant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.participant'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='category',
            field=models.CharField(choices=[('campus', 'campus'), ('senior', 'senior'), ('school', 'school')], max_length=10),
        ),
        migrations.AlterField(
            model_name='participant',
            name='district',
            field=models.CharField(choices=[('kollam', 'Kollam'), ('kottayam', 'Kottayam'), ('ernakulam', 'Ernakulam'), ('kannur', 'Kannur'), ('malappuram', 'Malappuram'), ('palakkad', 'Palakkad'), ('idukki', 'Idukki'), ('thiruvananthapuram', 'Thiruvananthapuram'), ('alappuzha', 'Alappuzha'), ('wayanad', 'Wayanad'), ('thrissur', 'Thrissur'), ('kasaragod', 'Kasaragod'), ('pathanamthitta', 'Pathanamthitta'), ('kozhikode', 'Kozhikode')], max_length=20),
        ),
    ]