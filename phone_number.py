import phonenumbers as pn
from phonenumbers import geocoder as gc
from phonenumbers import carrier as cr
from phonenumbers import timezone as tz

phone_number1 = pn.parse("+916366652685")
phone_number2 = pn.parse("+919353811901")
phone_number3 = pn.parse("+916364121443")
phone_number4 = pn.parse("+918618106931")

print("\n About the Phone Number\n")
print(phone_number1)
print(phone_number2)
print(phone_number3)
print(phone_number4)


print("\n Phone Numbers Location\n")
print(gc.description_for_number(phone_number1,"eng"))
print(gc.description_for_number(phone_number2,"eng"))
print(gc.description_for_number(phone_number3,"eng"))
print(gc.description_for_number(phone_number4,"eng"))

print("\n Finding the service provider\n")
print(cr.name_for_number(phone_number1,"eng"))
print(cr.name_for_number(phone_number2,"eng"))
print(cr.name_for_number(phone_number3,"eng"))
print(cr.name_for_number(phone_number4,"eng"))


print("\n Finding the Timezone of the given numbers\n")
print(tz.time_zones_for_geographical_number(phone_number1))
print(tz.time_zones_for_number(phone_number1))
print(tz.time_zones_for_geographical_number(phone_number2))
print(tz.time_zones_for_number(phone_number2))
print(tz.time_zones_for_geographical_number(phone_number3))
print(tz.time_zones_for_number(phone_number3))
print(tz.time_zones_for_geographical_number(phone_number4))
print(tz.time_zones_for_number(phone_number4))

print("\n Validating phone numbers\n")
print(pn.is_possible_number(phone_number2))
