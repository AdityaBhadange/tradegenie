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

"""
1. Add User id PK
2. Add multiple PK in one table
3. Create client table - id (ForiegnKey to all tables also)
4. Change whatsapp_number to social_number variable name
5. Create new Table - Productkeyword(user_id, keyword_id, product_id) (All are FK)
"""

class User(models.Model):
	user_id = models.AutoField(primary_key=True)
	email = models.EmailField(max_length=254, unique=True)
	mobile_number = models.CharField(max_length=20, unique=True)
	password = models.CharField(max_length=30)
	business_name = models.CharField(max_length=30, unique=True)
	city = models.CharField(max_length=30)
	user_type = models.CharField(max_length=1)
	social_number = models.CharField(max_length=20, unique=True)
	group = models.ForeignKey('Group', on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)

	def __repr__(self):
		return self.business_name


class SellerProfile(models.Model):
	# Add seller_id field manually
	# Add business_name field
	# Remove goole pay id
	# Remove google pay number
	seller_id = models.AutoField(primary_key=True)
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
	# Add keywork_id PK
	keywork_id = models.AutoField(primary_key=True)
	keyword_name = models.CharField(max_length=30)

	def __repr__(self):
		return self.keyword_name


# Change KeywordUser to UserInterest
# Auto generated pk field will be ok for this Table
class KeywordUser(models.Model):
	user = models.ForeignKey('User', on_delete=models.CASCADE)
	keyword = models.ForeignKey('Keyword', on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
	# Add product_id pk
	# Add field for youtube_link
	# Add product_name field
	product_id = models.AutoField(primary_key=True)
	user = models.ForeignKey('User', on_delete=models.CASCADE)
	catagory = models.ForeignKey('Catagory', on_delete=models.CASCADE)
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
	# catagory_id auto will be ok for this Table
	catagory_name = models.CharField(max_length=30)
	photo = models.ImageField(upload_to="images/")
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.catagory_name


class CategoryKeyword(models.Model):
	# Remove keyword field
	keyword = models.ForeignKey('Keyword', on_delete=models.CASCADE)
	catagory = models.ForeignKey('Catagory', on_delete=models.CASCADE)
	commission = models.DecimalField(max_digits=5, decimal_places=2)
	date = models.DateTimeField(auto_now_add=True)



class DeliveryPartner(models.Model):
	# Add id pk
	# Add address field
	delivery_partner_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


class Order(models.Model):
	# Add order_id pk
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
	# tracking_id = models.IntegerField(unique=True) # How to create pk for this? ---> ANswer - Charfield only
	delivery_partner = models.ForeignKey('DeliveryPartner', on_delete=models.CASCADE)
	shipment_date = models.DateTimeField(auto_now_add=True)
	group = models.ForeignKey('Group', on_delete=models.CASCADE)


class BuyerProfile(models.Model):
	# Add buyer_id pk
	buyer_id = models.AutoField(primary_key=True)
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
	# pk auto will be ok.
	order = models.ForeignKey('Order', on_delete=models.CASCADE)
	user = models.ForeignKey('User', on_delete=models.CASCADE)
	delivery_status = models.CharField(max_length=10)
	# tracking_id = models.DecimalField(unique=True) # How to create an ID for this field?
	shipment_date = models.DateTimeField(auto_now_add=True)


class Country(models.Model):
	country_name = models.CharField(max_length=20) # This should be pk
	date = models.DateTimeField(auto_now_add=True)

	def __repr__(self):
		return self.country_name


class City(models.Model):
	# change country_key to country_name
	city_name = models.CharField(max_length=20)
	country_key = models.ForeignKey('Country', on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)


class Tax(models.Model):
	# pk auto will be ok.
	# change country_key to country_name
	tax_name = models.CharField(max_length=30)
	tax_percentage = models.DecimalField(max_digits=5, decimal_places=2)
	country = models.ForeignKey('Country', on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)


class Notification(models.Model):
	user = models.ForeignKey('User', on_delete=models.CASCADE)
	notification_message = models.CharField(max_length=50) # make max_length=100
	date = models.DateTimeField(auto_now_add=True)


class Group(models.Model):
	# Add group_id pk
	group_id = models.AutoField(primary_key=True)
	group_name = models.CharField(max_length=20)
	group_description = models.CharField(max_length=50)
	date_of_addition = models.DateTimeField(auto_now_add=True) # Remove auto_add_now argument


class CommissionGroup(models.Model):
	# user should be removed
	group = models.ForeignKey('Group', on_delete=models.CASCADE)
	catagory = models.ForeignKey('Catagory', on_delete=models.CASCADE)
	company_commission = models.DecimalField(max_digits=5, decimal_places=2)
	group_commission = models.DecimalField(max_digits=5, decimal_places=2)
	user = models.ForeignKey('User', on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)


class Auth(models.Model):
	auth_id = models.AutoField(primary_key=True)
	user = models.ForeignKey('User', on_delete=models.CASCADE)
	super_admin = models.CharField(max_length=10) # Change to signel character / Make this BooleanFild
	group_admin = models.CharField(max_length=10) # Change to signel character / Make this BooleanFild
	delivery_admin = models.CharField(max_length=10)
	group = models.ForeignKey('Group', on_delete=models.CASCADE)
	screen_id_1 = models.BooleanField(default=False) # Make variable accroding to all the pages
	screen_id_2 = models.BooleanField(default=False)
	date = models.DateTimeField(auto_now_add=True)
