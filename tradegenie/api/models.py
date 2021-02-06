from django.db import models


"""
Author - Aditya Bhadange

Few Notes:-
	
	2. For the ForeignKey fields, I have changed the variable names (e.g. 'user_id' to 'user').
	3. Added '__repr__' function wherever necessery for readability.
	4. For phone numbers fields, I have used CharField.
	5. For images, I have used ImageField instead of FileField, because it checks for image formats.
"""

"""
###### CHANGES according to the meeting - 5 Feb 2021 ######
**DON'T DELETE THIS COMMENTS**

						*Changes*												*STATUS*

1. Added pk for all tables - 												(STATUS - DONE)
2. Add multiple PK in one table - 											(STATUS - Remaining)
4. Change whatsapp_number to social_number variable name - 					(STATUS - DONE)
5. Create new Table - Productkeyword(user_id, keyword_id, product_id)- 		(STATUS - DONE)
5. Create new Table - Client(client_id, date)- 								(STATUS - DONE)
"""

################################################################

#####################
#MASTER TABLE BELOW:-
#####################

class ProductKeyword(models.Model):
	"""
	This table is assigned to Shubhangi
	"""
	user = models.ForeignKey('User', on_delete=models.CASCADE)
	keyword = models.ForeignKey('Keyword', on_delete=models.CASCADE)
	product = models.ForeignKey('Product', on_delete=models.CASCADE)


class UserInterest(models.Model):
	"""
	This table is assigned to Devendra
	"""
	user = models.ForeignKey('User', on_delete=models.CASCADE)
	keyword = models.ForeignKey('Keyword', on_delete=models.CASCADE)
	client = models.ForeignKey('Client', on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)


class Client(models.Model):
	"""
	This table is assigned to Shubhangi
	"""
	client_id = models.AutoField(primary_key=True)
	date = models.DateTimeField(auto_now_add=True)



########################################################################



class User(models.Model):
	"""
	This table is assigned to Devendra
	"""
	user_id = models.AutoField(primary_key=True)
	email = models.EmailField(max_length=254, unique=True)
	mobile_number = models.CharField(max_length=20, unique=True)
	password = models.CharField(max_length=30)
	business_name = models.CharField(max_length=30, unique=True)
	city = models.CharField(max_length=30)
	user_type = models.CharField(max_length=1)
	social_number = models.CharField(max_length=20, unique=True)
	group = models.ForeignKey('Group', on_delete=models.CASCADE)
	client = models.ForeignKey('Client', on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)

	def __repr__(self):
		return self.business_name


class SellerProfile(models.Model):
	"""
	This table is assigned to Komal
	"""
	seller_id = models.AutoField(primary_key=True)
	user = models.ForeignKey('User', on_delete=models.CASCADE)
	business_name = models.CharField(max_length=30, unique=True)
	city = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	pin_code = models.CharField(max_length=10)
	social_number = models.CharField(max_length=20, unique=True)
	bank_name = models.CharField(max_length=30)
	bank_city = models.CharField(max_length=30)
	ifsc = models.CharField(max_length=10)
	branch_name = models.CharField(max_length=30)
	upi_id = models.CharField(max_length=20, unique=True)
	country = models.ForeignKey('Country', on_delete=models.CASCADE)
	group = models.ForeignKey('Group', on_delete=models.CASCADE)
	client = models.ForeignKey('Client', on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)


class Keyword(models.Model):
	"""
	This table is assigned to Aditya Bhadange
	"""
	keywork_id = models.AutoField(primary_key=True)
	keyword_name = models.CharField(max_length=30)
	client = models.ForeignKey('Client', on_delete=models.CASCADE)

	def __repr__(self):
		return self.keyword_name


class Product(models.Model):
	"""
	This table is assigned to Shubhangi
	"""
	product_id = models.AutoField(primary_key=True)
	user = models.ForeignKey('User', on_delete=models.CASCADE)
	product_name = models.CharField(max_length=20)
	catagory = models.ForeignKey('Catagory', on_delete=models.CASCADE)
	description = models.CharField(max_length=100)
	photos = models.ImageField(upload_to="images/")
	youtube_link = models.URLField()
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
	client = models.ForeignKey('Client', on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)


class Catagory(models.Model):
	"""
	This table is assigned to Sudarshan
	"""
	catagory_name = models.CharField(max_length=30)
	photo = models.ImageField(upload_to="images/")
	client = models.ForeignKey('Client', on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.catagory_name


class CategoryKeyword(models.Model):
	"""
	This table is assigned to Sudarshan
	"""
	catagory = models.ForeignKey('Catagory', on_delete=models.CASCADE)
	commission = models.DecimalField(max_digits=5, decimal_places=2)
	client = models.ForeignKey('Client', on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)


class DeliveryPartner(models.Model):
	"""
	This table is assigned to Shubhangi
	"""
	delivery_partner_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	client = models.ForeignKey('Client', on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


class Order(models.Model):
	"""
	This table is assigned to Aditya Bhadange
	"""
	order_id = models.AutoField(primary_key=True)
	date_of_order = models.DateTimeField(auto_now_add=True)
	product = models.ForeignKey('Product', on_delete=models.CASCADE)
	seller = models.ForeignKey('SellerProfile', on_delete=models.CASCADE)
	buyer = models.ForeignKey('BuyerProfile', on_delete=models.CASCADE)
	quantity = models.DecimalField(max_digits=5, decimal_places=2)
	basic_cost = models.DecimalField(max_digits=5, decimal_places=2)
	tax = models.DecimalField(max_digits=5, decimal_places=2)
	delivery_cost = models.DecimalField(max_digits=5, decimal_places=2)
	total_cost = models.DecimalField(max_digits=5, decimal_places=2)
	status = models.CharField(max_length=10)
	tracking_id = models.CharField(max_length=100)
	delivery_partner = models.ForeignKey('DeliveryPartner', on_delete=models.CASCADE)
	shipment_date = models.DateTimeField(auto_now_add=True)
	client = models.ForeignKey('Client', on_delete=models.CASCADE)
	group = models.ForeignKey('Group', on_delete=models.CASCADE)


class BuyerProfile(models.Model):
	"""
	This table is assigned to Komal
	"""
	buyer_id = models.AutoField(primary_key=True)
	user = models.ForeignKey('User', on_delete=models.CASCADE)
	delivery_name = models.CharField(max_length=30)
	delivery_city = models.CharField(max_length=30)
	delivery_address = models.CharField(max_length=50)
	delivery_pin_code = models.DecimalField(max_digits=5, decimal_places=2)
	delivery_social_number = models.CharField(max_length=20)
	billing_name = models.CharField(max_length=30)
	billing_city = models.CharField(max_length=30)
	billing_address = models.CharField(max_length=50)
	billing_pin_code = models.DecimalField(max_digits=5, decimal_places=2)
	billing_social_number = models.CharField(max_length=20)
	client = models.ForeignKey('Client', on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)


class DeliveryPartnerOrder(models.Model):
	"""
	This table is assigned to Aditya
	"""
	order = models.ForeignKey('Order', on_delete=models.CASCADE)
	user = models.ForeignKey('User', on_delete=models.CASCADE)
	delivery_status = models.CharField(max_length=10)
	tracking_id = models.CharField(max_length=100)
	client = models.ForeignKey('Client', on_delete=models.CASCADE)
	shipment_date = models.DateTimeField(auto_now_add=True)


class Country(models.Model):
	"""
	This table is assigned to Ajay
	"""
	country_name = models.CharField(max_length=20, primary_key=True)
	client = models.ForeignKey('Client', on_delete=models.CASCADE)

	def __repr__(self):
		return self.country_name


class City(models.Model):
	"""
	This table is assigned to Chitra
	"""
	city_name = models.CharField(max_length=20, primary_key=True)
	country_name = models.ForeignKey('Country', on_delete=models.CASCADE)
	client = models.ForeignKey('Client', on_delete=models.CASCADE)


class Tax(models.Model):
	"""
	This table is assigned to Chitra
	"""
	tax_name = models.CharField(max_length=30)
	tax_percentage = models.DecimalField(max_digits=5, decimal_places=2)
	country = models.ForeignKey('Country', on_delete=models.CASCADE)
	client = models.ForeignKey('Client', on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)


class Notification(models.Model):
	"""
	This table is assigned to Nilesh
	"""
	user = models.ForeignKey('User', on_delete=models.CASCADE)
	notification_message = models.CharField(max_length=100)
	client = models.ForeignKey('Client', on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)


class Group(models.Model):
	"""
	This table is assigned to Shreyas
	"""
	group_id = models.AutoField(primary_key=True)
	group_name = models.CharField(max_length=20)
	group_description = models.CharField(max_length=50)
	client = models.ForeignKey('Client', on_delete=models.CASCADE)
	date_of_addition = models.DateTimeField()


class CommissionGroup(models.Model):
	"""
	This table is assigned to Nilesh
	"""
	group = models.ForeignKey('Group', on_delete=models.CASCADE)
	catagory = models.ForeignKey('Catagory', on_delete=models.CASCADE)
	company_commission = models.DecimalField(max_digits=5, decimal_places=2)
	group_commission = models.DecimalField(max_digits=5, decimal_places=2)
	client = models.ForeignKey('Client', on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)


class Auth(models.Model):
	"""
	This table is assigned to Nilesh
	"""
	auth_id = models.AutoField(primary_key=True)
	user = models.ForeignKey('User', on_delete=models.CASCADE)
	super_admin = models.BooleanField(default=False)
	group_admin = models.BooleanField(default=False)
	delivery_admin = models.CharField(max_length=10)
	group = models.ForeignKey('Group', on_delete=models.CASCADE)
	page_adminpanel = models.BooleanField(default=False)
	page_dashboard = models.BooleanField(default=False)
	page_user = models.BooleanField(default=False)
	page_order = models.BooleanField(default=False)
	page_catagory = models.BooleanField(default=False)
	page_product = models.BooleanField(default=False)
	page_country = models.BooleanField(default=False)
	page_tax = models.BooleanField(default=False)
	page_commission = models.BooleanField(default=False)
	page_groups = models.BooleanField(default=False)
	page_payment = models.BooleanField(default=False)
	page_keyword = models.BooleanField(default=False)
	client = models.ForeignKey('Client', on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)
