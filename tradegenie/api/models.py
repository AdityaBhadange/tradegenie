from django.db import models


"""
Author - Aditya Bhadange

Few Notes:-
	
	1. Removed all the pk columns, bcs Django adds it for all the tables automatically.
	2. For the ForeignKey fields, I have changed the variable names (e.g. 'user_id' to 'user').
	3. Added '__repr__' function wherever necessery for readability.
	4. For phone numbers fields, I have used CharField.
	5. For images, I have used ImageField instead of FileField, because it checks for image formats.
"""


class User(models.Model):
	email = models.EmailField(max_length=254, unique=True)
	mobile_number = models.CharField(max_length=20, unique=True)
	password = models.CharField(max_length=30)
	business_name = models.CharField(max_length=30, unique=True)
	city = models.CharField(max_length=30)
	seller = models.CharField(max_length=1)
	whatsapp_number = models.CharField(max_length=20, unique=True)
	group = models.ForeignKey('Group', on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)

	def __repr__(self):
		return self.business_name


class SellerProfile(models.Model):
	user = models.ForeignKey('User', on_delete=models.CASCADE)
	city = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	pin_code = models.CharField(max_length=10)
	whatsapp_number = models.CharField(max_length=20, unique=True)
	bank_name = models.CharField(max_length=30)
	bank_city = models.CharField(max_length=30)
	ifsc = models.CharField(max_length=10)
	branch_name = models.CharField(max_length=30)
	google_pay_id = models.CharField(max_length=30, unique=True)
	upi_id = models.CharField(max_length=20, unique=True)
	google_pay_number = models.CharField(max_length=20, unique=True)
	country = models.ForeignKey('Country', on_delete=models.CASCADE)
	group = models.ForeignKey('Group', on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)


class Keyword(models.Model):
	keyword_name = models.CharField(max_length=30)

	def __repr__(self):
		return self.keyword_name


class KeywordUser(models.Model):
	user = models.ForeignKey('User', on_delete=models.CASCADE)
	keyword = models.ForeignKey('Keyword', on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
	user = models.ForeignKey('User', on_delete=models.CASCADE)
	catagory_id = models.ForeignKey('Catagory', on_delete=models.CASCADE)
	description = models.CharField(max_length=100)
	photos = models.ImageField(upload_to="images/")
	gst = models.CharField(max_length=30)
	courier_self = models.CharField(max_length=30)
	self_delivery_cost = models.DecimalField(max_digits=5, decimal_places=2)
	delivery_partner = models.ForeignKey('DeliveryPartner', on_delete=models.CASCADE)
	length = models.DecimalField(max_digits=5, decimal_places=2)
	width = models.DecimalField(max_digits=5, decimal_places=2)
	height = models.DecimalField(max_digits=5, decimal_places=2)
	weight = models.DecimalField(max_digits=5, decimal_places=2)
	delivery_partner_cost = models.DecimalField(max_digits=5, decimal_places=2)
	product_cost = models.DecimalField(max_digits=5, decimal_places=2)
	date = models.DateTimeField(auto_now_add=True)


class Catagory(models.Model):
	catagory_name = models.CharField(max_length=30)
	photo = models.ImageField(upload_to="images/")
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.catagory_name


class CategoryKeyword(models.Model):
	keyword = models.ForeignKey('Keyword', on_delete=models.CASCADE)
	catagory = models.ForeignKey('Catagory', on_delete=models.CASCADE)
	commission = models.DecimalField(max_digits=5, decimal_places=2)
	date = models.DateTimeField(auto_now_add=True)



class DeliveryPartner(models.Model):
	name = models.CharField(max_length=30)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


class Order(models.Model):
	date_of_order = models.DateTimeField(auto_now_add=True)
	product = models.ForeignKey('product', on_delete=models.CASCADE)
	seller = models.ForeignKey('SellerProfile', on_delete=models.CASCADE)
	buyer = models.ForeignKey('BuyerProfile', on_delete=models.CASCADE)
	quantity = models.DecimalField(max_digits=5, decimal_places=2)
	basic_cost = models.DecimalField(max_digits=5, decimal_places=2)
	tax = models.DecimalField(max_digits=5, decimal_places=2)
	delivery_cost = models.DecimalField(max_digits=5, decimal_places=2)
	total_cost = models.DecimalField(max_digits=5, decimal_places=2)
	status = models.CharField(max_length=10)
	# tracking_id = models.IntegerField(unique=True) # How to create pk for this?
	delivery_partner = models.ForeignKey('DeliveryPartner', on_delete=models.CASCADE)
	shipment_date = models.DateTimeField(auto_now_add=True)
	group = models.ForeignKey('Group', on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)


class BuyerProfile(models.Model):
	user = models.ForeignKey('User', on_delete=models.CASCADE)
	delivery_name = models.CharField(max_length=30)
	delivery_city = models.CharField(max_length=30)
	delivery_address = models.CharField(max_length=50)
	delivery_pin_code = models.DecimalField(max_digits=5, decimal_places=2)
	delivery_whatsapp_number = models.CharField(max_length=20)
	billing_name = models.CharField(max_length=30)
	billing_city = models.CharField(max_length=30)
	billing_address = models.CharField(max_length=50)
	billing_pin_code = models.DecimalField(max_digits=5, decimal_places=2)
	billing_whatsapp_number = models.CharField(max_length=20)
	date = models.DateTimeField(auto_now_add=True)


class DeliveryPartnerOrder(models.Model):
	order = models.ForeignKey('Order', on_delete=models.CASCADE)
	user = models.ForeignKey('User', on_delete=models.CASCADE)
	delivery_status = models.CharField(max_length=10)
	# tracking_id = models.DecimalField(unique=True) # How to create an ID for this field?
	shipment_date = models.DateTimeField(auto_now_add=True)


class Country(models.Model):
	country_name = models.CharField(max_length=20)
	date = models.DateTimeField(auto_now_add=True)

	def __repr__(self):
		return self.country_name


class City(models.Model):
	city_name = models.CharField(max_length=20)
	country_key = models.ForeignKey('Country', on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)


class Tax(models.Model):
	tax_name = models.CharField(max_length=30)
	tax_percentage = models.DecimalField(max_digits=5, decimal_places=2)
	country = models.ForeignKey('Country', on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)


class Notification(models.Model):
	user = models.ForeignKey('User', on_delete=models.CASCADE)
	notification_message = models.CharField(max_length=50)
	date = models.DateTimeField(auto_now_add=True)


class Group(models.Model):
	group_description = models.CharField(max_length=50)
	date_of_addition = models.DateTimeField(auto_now_add=True)


class CommissionGroup(models.Model):
	group = models.ForeignKey('Group', on_delete=models.CASCADE)
	catagory = models.ForeignKey('Catagory', on_delete=models.CASCADE)
	company_commission = models.DecimalField(max_digits=5, decimal_places=2)
	group_commission = models.DecimalField(max_digits=5, decimal_places=2)
	user = models.ForeignKey('User', on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)


class Auth(models.Model):
	user = models.ForeignKey('User', on_delete=models.CASCADE)
	super_admin = models.CharField(max_length=10)
	group_admin = models.CharField(max_length=10)
	delivery_admin = models.CharField(max_length=10)
	group = models.ForeignKey('Group', on_delete=models.CASCADE)
	screen_id_1 = models.BooleanField(default=False)
	screen_id_2 = models.BooleanField(default=False)
	date = models.DateTimeField(auto_now_add=True)
