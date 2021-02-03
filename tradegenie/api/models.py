from django.db import models


class User(models.Model):
	email = models.EmailField(max_length=254, unique=True)
	mobile_number = models.CharField(max_length=20, unique=True)
	password = models.CharField(max_length=30)
	business_name = models.CharField(max_length=30, unique=True)
	city = models.CharField(max_length=30)
	seller = models.CharField(max_length=1)
	whatsapp_number = models.CharField(max_length=20, unique=True)
	group = models.ForeignKey(Group, on_delete=CASCADE)
	date = models.DateTimeField(auto_now_add=True)

	class __repr__(self):
		return self.business_name


class SellerProfile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	city = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	pin_code = models.CharField(max_length=10)
	whatsapp_number = models.CharField(max_length=20, unique=True)
	bank_name = models.CharField(max_length=30)
	bank_city = models.CharField(max_length=30)
	ifsc = models.CharField(max_length=10)
	branch_name = models.CharField(max_length=30)
	google_pay_id = models.CharField(max_length=30, unique=True)
	upi_id = models.CharField(max_length=30, unique=True)
	google_pay_number = models.CharField(max_length=20, unique=True)
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	group = models.ForeignKey(Group, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)


# class Keyword(models.Model):
# 	keyword_id = models.IntegerField(primary_key=True)
# 	keyword_name = models.CharField(max_length=30)

# 	class Meta:
# 		db_table = "KeywordTable"


# class KeywordUser(models.Model):
# 	mapping_id = models.AutoField(primary_key=True)
# 	user = models.ForeignKey(primary_key=True)
# 	keyword_id = models.ForeignKey(primary_key=True)

# 	class Meta:
# 		db_table = "KeywordUser"


# class Product(models.Model):
# 	product_id = models.AutoField(primary_key=True)
# 	user = models.ForeignKey()
# 	catagory_id = models.ForeignKey()
# 	description = models.CharField(max_length=100)
# 	photos = models.FileField(upload_to="uploads/")
# 	gst = models.CharField(max_length=30)
# 	courier_self = models.CharField(max_length=30)
# 	self_delivery_cost = models.IntegerField()
# 	delivery_partner_id = models.ForeignKey("", on_delete=models.CASCADE)
# 	length = models.IntegerField() # Query
# 	width = models.IntegerField() # Query
# 	height = models.AutoField() # Query
# 	weight = models.IntegerField(max_length=30)
# 	delivery_partner_cost = models.IntegerField()
# 	product_cost = models.IntegerField()

# 	class Meta:
# 		db_table = "ProductTable"


# class Catagory(models.Model):
# 	catagory_id = models.AutoField(primary_key=True)
# 	catagory_name = models.CharField(max_length=30)
# 	photo = models.FileField(upload_to="uploads/")


# class CategoryKeyword(models.Model):
# 	table_primary_key = models.AutoField(primary_key=True)
# 	keyword_id = models.ForeignKey()
# 	catagory_id = models.ForeignKey()
# 	commission = models.IntegerField()

# 	class Meta:
# 		db_table = "CategoryKeyword"


# class DeliveryPartnerTable(models.Model):
# 	delivery_partner_id = models.AutoField(primary_key=True)
# 	name = models.CharField(max_length=30)

# 	class Meta:
# 		db_table = "DeliveryPartnerTable"


# class Order(models.Model):
# 	order_id = models.AutoField(primary_key=True)
# 	date_of_order = models.AutoField()
# 	product_id = models.ForeignKey()
# 	seller_id = models.ForeignKey()
# 	buyer_id = models.ForeignKey()
# 	quantity = models.IntegerField()
# 	basic_cost = models.IntegerField()
# 	tax = models.IntegerField()
# 	delivery_cost = models.IntegerField()
# 	total_cost = models.IntegerField()
# 	status = models.CharField() # Query
# 	tracking_id = models.IntegerField(unique=True)
# 	delivery_partner_id = models.IntegerField()
# 	shipment_date = models.DateTimeField()
# 	group_id = models.ForeignKey()

# 	class Meta:
# 		db_table = "OrderTable"


# class BuyerProfile(models.Model):
# 	buyer_id = models.AutoField(primary_key=True)
# 	user = models.ForeignKey()
# 	delivery_name = models.CharField(max_length=30)
# 	delivery_city = models.CharField(max_length=30)
# 	delivery_address = models.CharField(max_length=50)
# 	delivery_pin_code = models.IntegerField()
# 	delivery_whatsapp_number = models.IntegerField()
# 	billing_name = models.CharField(max_length=30)
# 	billing_city = models.AutoField()
# 	billing_address = models.AutoField()
# 	billing_pin = models.AutoField()
# 	billing_whatsapp_number = models.AutoField()

# 	class Meta:
# 		db_table = "BuyerProfile"


# class DeliveryPartnerOrder(models.Model):
# 	table_key = models.AutoField(primary_key=True)
# 	order_id = models.ForeignKey()
# 	user = models.ForeignKey()
# 	delivery_status = models.CharField(max_length=30)
# 	tracking_id = models.IntegerField(unique=True)
# 	shipment_date = models.DateTimeField()

# 	class Meta:
# 		db_table = "DeliveryPartnerOrderTable"


# class Country(models.Model):
# 	country_key = models.AutoField(primary_key=True)
# 	country_name = models.CharField(max_length=30)

# 	class Meta:
# 		db_table = "CountryTable"


# class City(models.Model):
# 	city_key = models.AutoField(primary_key=True)
# 	city_name = models.AutoField(primary_key=True)
# 	country_key = models.ForeignKey()


# class Tax(models.Model):
# 	tax_id = models.AutoField(primary_key=True)
# 	tax_name = models.CharField(max_length=30)
# 	tax_percentage = models.CharField(max_length=30)
# 	tax_name = models.CharField(max_length=30)


# class Notification(models.Model):
# 	notification_id = models.AutoField(primary_key=True)
# 	user = models.ForeignKey()
# 	notification_message = models.CharField(max_length=50)


# class Group(models.Model):
# 	group_id = models.AutoField(primary_key=True)
# 	group_description = models.CharField(max_length=50)
# 	date_of_addition = models.DateTimeField()


# class CommissionGroup(models.Model):
# 	table_key = models.AutoField(primary_key=True)
# 	group_id = models.ForeignKey()
# 	catagory_id = models.IntegerField(unique=True)
# 	company_commission = models.IntegerField()
# 	group_commission = models.IntegerField()
# 	user = models.ForeignKey()


# class Auth(models.Model):
# 	table_key = models.AutoField(primary_key=True)
# 	user = models.ForeignKey()
# 	super_admin = models.CharField()
# 	group_admin = models.CharField()
# 	delivery_admin = models.CharField()
# 	group_id = models.ForeignKey()
# 	screen_id_1 = models.IntegerField(unique=True)
# 	screen_id_2 = models.IntegerField(unique=True)
