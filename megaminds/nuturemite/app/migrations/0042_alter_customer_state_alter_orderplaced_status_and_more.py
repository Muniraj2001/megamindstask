# Generated by Django 4.2.7 on 2023-12-05 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_alter_customer_state_alter_orderplaced_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Chandigarh', 'Chandigarh'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Haryana', 'Haryana'), ('Chattisgarh', 'Chattisgarh'), ('Daman and Diu', 'Daman and Diu'), ('Goa', 'Goa'), ('Delhi', 'Delhi'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Assam', 'Assam'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Gujrat', 'Gujrat'), ('Bihar', 'Bihar')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'packed'), ('Delivered', 'Delivered'), ('On The Wey', 'On The Way'), ('Cancel', 'Cancel'), ('Pending', 'Pending')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='popular',
            name='category',
            field=models.CharField(choices=[('WH', 'Women health'), ('GH', 'General Health'), ('IH', 'Immune Health'), ('VM', 'Vitamins&Minerals'), ('MH', 'Men Health'), ('SH', 'Sexual health'), ('HS', 'Herbal, Specialty Supplements'), ('AV', 'Ayurvedic'), ('AN', 'Antioxidants'), ('PC', 'Personal Care'), ('DH', 'Digestive Health'), ('OG', 'Organic')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('WH', 'Women health'), ('GH', 'General Health'), ('IH', 'Immune Health'), ('VM', 'Vitamins&Minerals'), ('MH', 'Men Health'), ('SH', 'Sexual health'), ('HS', 'Herbal, Specialty Supplements'), ('AV', 'Ayurvedic'), ('AN', 'Antioxidants'), ('PC', 'Personal Care'), ('DH', 'Digestive Health'), ('OG', 'Organic')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product1',
            name='category',
            field=models.CharField(choices=[('WH', 'Women health'), ('GH', 'General Health'), ('IH', 'Immune Health'), ('VM', 'Vitamins&Minerals'), ('MH', 'Men Health'), ('SH', 'Sexual health'), ('HS', 'Herbal, Specialty Supplements'), ('AV', 'Ayurvedic'), ('AN', 'Antioxidants'), ('PC', 'Personal Care'), ('DH', 'Digestive Health'), ('OG', 'Organic')], max_length=2),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='category',
            field=models.CharField(choices=[('WH', 'Women health'), ('GH', 'General Health'), ('IH', 'Immune Health'), ('VM', 'Vitamins&Minerals'), ('MH', 'Men Health'), ('SH', 'Sexual health'), ('HS', 'Herbal, Specialty Supplements'), ('AV', 'Ayurvedic'), ('AN', 'Antioxidants'), ('PC', 'Personal Care'), ('DH', 'Digestive Health'), ('OG', 'Organic')], max_length=2),
        ),
    ]
