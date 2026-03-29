# Bothive - Business Profile Card
# Task: create a profile for the first business on Bothive

# --- Business Information ---
business_name = "The Coffee Spot"
business_id = 1001
owner_name = "Sameer Wadhane"
city = "Pune"
Phone_number = "91-1234567890"
email = "sameer.wadhane@example.com"
monthly_plan_price = 999.99
is_verified = True
bot_active = False
total_messages_handled = 0
rating = float(input("Enter the business rating (1-5): "))
# --- Print the Business Profile ---
print("=" * 40)             
print("BOTHIVE — BUSINESS PROFILE")
print("=" * 40)
print(f"Business Name: {business_name}")
print(f"Business ID: {business_id}")
print(f"Owner Name: {owner_name}")
print(f"City: {city}")
print(f"Phone Number: {Phone_number}")
print(f"Email: {email}")
print(f"Monthly Plan: Rs. {monthly_plan_price}")
print(f"Verified       : {is_verified}")
print(f"Bot Active     : {bot_active}")
print(f"Messages Today : {total_messages_handled}")
print(f"Rating         : {rating} / 5.0")
print("=" * 40)

print("\nData Types:")
print(f"business_name is a {type(business_name).__name__}")
print(f"business_id is an {type(business_id).__name__}")
print(f"monthly_plan_price is a {type(monthly_plan_price).__name__}")
print(f"is_verified is a {type(is_verified).__name__}")
print(f"bot_active is a {type(bot_active).__name__}")