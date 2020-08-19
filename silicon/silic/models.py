
from django.db import models


class Registration(models.Model):
 First_name = models.CharField(max_length=200)
 Last_name = models.CharField(max_length=200)
 Email = models.EmailField(max_length=200)
 Phone = models.CharField(max_length=12)
 Password = models.CharField(max_length=200)
 State = models.CharField(max_length=200)
 City = models.CharField(max_length=200)
 Pincode = models.IntegerField()
 Address = models.TextField()
 About = models.TextField()
 Lock = models.CharField(max_length=200)
class Pre_order(models.Model):
 Category_name = models.CharField(max_length=200)
 Product_name = models.CharField(max_length=200)
 Price = models.FloatField()
 First_name = models.CharField(max_length=200)
 Last_name = models.CharField(max_length=200)
 Email = models.EmailField(max_length=200)
 Phone = models.CharField(max_length=12)
 State = models.CharField(max_length=200)
 City = models.CharField(max_length=200)
 Pincode = models.BigIntegerField()
 Address = models.TextField()
 Quantity = models.IntegerField()
 Order_date = models.DateField(auto_now_add=True)
 Total_amount = models.FloatField()
 Order_status = models.CharField(max_length=200)
class Cust_cart(models.Model):
 Front_message = models.CharField(max_length=200)
 Back_message = models.CharField(max_length=200)
 Color = models.CharField(max_length=200)
 Fon_style = models.CharField(max_length=200)
 Ban_size = models.FloatField()
 Ban_style = models.CharField(max_length=200)
 Clippart_name = models.CharField(max_length=200)
 QQuantity = models.BigIntegerField()
 Pricce = models.FloatField()
 Total_amount = models.FloatField()
 Delivery_charge = models.FloatField()
 regg = models.ForeignKey(Registration,on_delete=models.CASCADE)
class Band_order(models.Model):
 Front_message = models.CharField(max_length=200)
 Back_message = models.CharField(max_length=200)
 Color = models.CharField(max_length=200)
 Fonts_style = models.CharField(max_length=200)
 Bandd_size = models.CharField(max_length=200)
 Bandd_style = models.CharField(max_length=200)
 Clipartt_name = models.CharField(max_length=200)
 Quantitty = models.BigIntegerField()
 Pricee = models.FloatField()
 Totall_amount = models.FloatField()
 First_name = models.CharField(max_length=200)
 Last_name = models.CharField(max_length=200)
 Email = models.EmailField(max_length=200)
 Phone = models.CharField(max_length=12)
 State = models.CharField(max_length=200)
 City = models.CharField(max_length=200)
 Pincode = models.BigIntegerField()
 Address = models.TextField()
 Order_date = models.DateField(auto_now_add=True)
 Order_status = models.CharField(max_length=200)
class Faq(models.Model):
 Customer_name = models.CharField(max_length=200)
 Customer_email = models.EmailField()
 Question = models.TextField()
 Answer = models.TextField()
 Submission_date = models.DateField(auto_now_add=True)
class Quotation_cus(models.Model):
 Customer_name = models.CharField(max_length=200)
 Customer_email = models.EmailField()
 Category_name = models.CharField(max_length=200)
 Description = models.TextField()
 Quantity_selected = models.BigIntegerField()
 Quotation_date = models.DateField(auto_now_add=True)
 Status = models.CharField(max_length=200)
class Band_details(models.Model):
 Size_in_inch = models.FloatField()
 Style = models.CharField(max_length=200)
 Clipart_name = models.CharField(max_length=200)
 Clipart_image = models.ImageField()
 Font_name = models.CharField(max_length=200)
 Minimum_quantity = models.BigIntegerField()
 Maximum_quantity = models.BigIntegerField()
 Discount_percentage = models.FloatField()
 Unit_price = models.IntegerField()
 Status = models.CharField(max_length=200)
class Conveyance_fees(models.Model):
 Delivery_charge_min_km = models.BigIntegerField()
 Delivery_charge_max_km = models.BigIntegerField()
 Delivery_fees = models.FloatField()
 Shipping_days = models.BigIntegerField()
 Shipping_description = models.TextField()
 Shipping_cost = models.FloatField()
 Status = models.CharField(max_length=200)
class Category_product(models.Model):
 Category_name = models.CharField(max_length=200)
 Product_name = models.CharField(max_length=200)
 Product_image = models.ImageField()
 Minimum_quantity = models.BigIntegerField()
 Maximum_quantity = models.BigIntegerField()
 Discount_percentage = models.FloatField()
 Unit_price = models.FloatField()
 Status = models.CharField(max_length=200)
class Quotation(models.Model):
 Category_name = models.CharField(max_length=200)
 Minimum_quantity = models.BigIntegerField()
 Maximum_quantity = models.BigIntegerField()
 Discount_percent = models.FloatField()
 Status = models.CharField(max_length=200)
 catt = models.ForeignKey(Category_product, on_delete=models.CASCADE)
class Feedback(models.Model):
 Name = models.CharField(max_length=200)
 Email = models.EmailField()
 Category = models.CharField(max_length=200)
 Content = models.TextField()
 Submission_date = models.DateField(auto_now_add = True)