# Generated by Django 4.2.7 on 2024-01-02 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0080_pincode_alter_customer_state_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderplaced',
            name='pincode',
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Daman and Diu', 'Daman and Diu'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Delhi', 'Delhi'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Chattisgarh', 'Chattisgarh'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Goa', 'Goa'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Assam', 'Assam'), ('Haryana', 'Haryana'), ('Chandigarh', 'Chandigarh'), ('Bihar', 'Bihar'), ('Gujrat', 'Gujrat')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Delivered', 'Delivered'), ('On The Wey', 'On The Way'), ('Cancel', 'Cancel'), ('Accepted', 'Accepted'), ('Packed', 'packed')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='popular',
            name='category',
            field=models.CharField(choices=[('AV', 'Ayurvedic'), ('C', 'Vitamin C'), ('A', 'Vitamin A'), ('HS', 'Herbal, Specialty Supplements'), ('SH', 'Sexual health'), ('OG', 'Organic'), ('K', 'Vitamin K'), ('E', 'Vitamin E'), ('GH', 'General Health'), ('PC', 'Personal Care'), ('VM', 'Vitamins&Minerals'), ('WH', 'Women health'), ('D3', 'Vitamin D3'), ('MH', 'Men Health'), ('AN', 'Antioxidants'), ('IH', 'Immune Health'), ('DH', 'Digestive Health'), ('B12', 'Vitamin B12')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('AV', 'Ayurvedic'), ('C', 'Vitamin C'), ('A', 'Vitamin A'), ('HS', 'Herbal, Specialty Supplements'), ('SH', 'Sexual health'), ('OG', 'Organic'), ('K', 'Vitamin K'), ('E', 'Vitamin E'), ('GH', 'General Health'), ('PC', 'Personal Care'), ('VM', 'Vitamins&Minerals'), ('WH', 'Women health'), ('D3', 'Vitamin D3'), ('MH', 'Men Health'), ('AN', 'Antioxidants'), ('IH', 'Immune Health'), ('DH', 'Digestive Health'), ('B12', 'Vitamin B12')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product1',
            name='category',
            field=models.CharField(choices=[('AV', 'Ayurvedic'), ('C', 'Vitamin C'), ('A', 'Vitamin A'), ('HS', 'Herbal, Specialty Supplements'), ('SH', 'Sexual health'), ('OG', 'Organic'), ('K', 'Vitamin K'), ('E', 'Vitamin E'), ('GH', 'General Health'), ('PC', 'Personal Care'), ('VM', 'Vitamins&Minerals'), ('WH', 'Women health'), ('D3', 'Vitamin D3'), ('MH', 'Men Health'), ('AN', 'Antioxidants'), ('IH', 'Immune Health'), ('DH', 'Digestive Health'), ('B12', 'Vitamin B12')], max_length=3),
        ),
        migrations.AlterField(
            model_name='shopnow',
            name='category',
            field=models.CharField(choices=[('AV', 'Ayurvedic'), ('C', 'Vitamin C'), ('A', 'Vitamin A'), ('HS', 'Herbal, Specialty Supplements'), ('SH', 'Sexual health'), ('OG', 'Organic'), ('K', 'Vitamin K'), ('E', 'Vitamin E'), ('GH', 'General Health'), ('PC', 'Personal Care'), ('VM', 'Vitamins&Minerals'), ('WH', 'Women health'), ('D3', 'Vitamin D3'), ('MH', 'Men Health'), ('AN', 'Antioxidants'), ('IH', 'Immune Health'), ('DH', 'Digestive Health'), ('B12', 'Vitamin B12')], max_length=3),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='category',
            field=models.CharField(choices=[('AV', 'Ayurvedic'), ('C', 'Vitamin C'), ('A', 'Vitamin A'), ('HS', 'Herbal, Specialty Supplements'), ('SH', 'Sexual health'), ('OG', 'Organic'), ('K', 'Vitamin K'), ('E', 'Vitamin E'), ('GH', 'General Health'), ('PC', 'Personal Care'), ('VM', 'Vitamins&Minerals'), ('WH', 'Women health'), ('D3', 'Vitamin D3'), ('MH', 'Men Health'), ('AN', 'Antioxidants'), ('IH', 'Immune Health'), ('DH', 'Digestive Health'), ('B12', 'Vitamin B12')], max_length=3),
        ),
        migrations.DeleteModel(
            name='Pincode',
        ),
    ]
