# Generated by Django 4.2.7 on 2023-11-26 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_alter_customer_state_alter_orderplaced_status_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post1',
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Arunachal Pradesh', 'Arunachal Pradesh'), ('Haryana', 'Haryana'), ('Delhi', 'Delhi'), ('Gujrat', 'Gujrat'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Assam', 'Assam'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Chandigarh', 'Chandigarh'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Goa', 'Goa'), ('Chattisgarh', 'Chattisgarh'), ('Bihar', 'Bihar'), ('Daman and Diu', 'Daman and Diu')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Cancel', 'Cancel'), ('Packed', 'packed'), ('Accepted', 'Accepted'), ('Delivered', 'Delivered'), ('On The Wey', 'On The Way'), ('Pending', 'Pending')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='popular',
            name='category',
            field=models.CharField(choices=[('IH', 'Immune Health'), ('VM', 'Vitamins&Minerals'), ('GH', 'General Health'), ('AN', 'Antioxidants'), ('SH', 'Sexual health'), ('MH', 'Men Health'), ('DH', 'Digestive Health'), ('AV', 'Ayurvedic'), ('PC', 'Personal Care'), ('HS', 'Herbal, Specialty Supplements'), ('WH', 'Women health'), ('OG', 'Organic')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('IH', 'Immune Health'), ('VM', 'Vitamins&Minerals'), ('GH', 'General Health'), ('AN', 'Antioxidants'), ('SH', 'Sexual health'), ('MH', 'Men Health'), ('DH', 'Digestive Health'), ('AV', 'Ayurvedic'), ('PC', 'Personal Care'), ('HS', 'Herbal, Specialty Supplements'), ('WH', 'Women health'), ('OG', 'Organic')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product1',
            name='category',
            field=models.CharField(choices=[('IH', 'Immune Health'), ('VM', 'Vitamins&Minerals'), ('GH', 'General Health'), ('AN', 'Antioxidants'), ('SH', 'Sexual health'), ('MH', 'Men Health'), ('DH', 'Digestive Health'), ('AV', 'Ayurvedic'), ('PC', 'Personal Care'), ('HS', 'Herbal, Specialty Supplements'), ('WH', 'Women health'), ('OG', 'Organic')], max_length=2),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='category',
            field=models.CharField(choices=[('IH', 'Immune Health'), ('VM', 'Vitamins&Minerals'), ('GH', 'General Health'), ('AN', 'Antioxidants'), ('SH', 'Sexual health'), ('MH', 'Men Health'), ('DH', 'Digestive Health'), ('AV', 'Ayurvedic'), ('PC', 'Personal Care'), ('HS', 'Herbal, Specialty Supplements'), ('WH', 'Women health'), ('OG', 'Organic')], max_length=2),
        ),
    ]
