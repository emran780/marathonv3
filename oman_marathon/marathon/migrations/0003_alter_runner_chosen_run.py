# Generated by Django 4.2.7 on 2023-12-03 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marathon', '0002_contactusmessage_remove_runregistration_run_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runner',
            name='chosen_run',
            field=models.CharField(blank=True, choices=[('5K', '5K'), ('10K', '10K'), ('Kids', 'Kids'), ('none', 'none')], max_length=50, null=True),
        ),
    ]
