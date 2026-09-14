from address import Address
from mailing import Mailing

to_addr = Address(индекс="123456", город="Москва", улица="Ленина", дом="10", квартира="50а")
from_addr = Address(индекс="678901", город="Санкт-Петербург", улица="Мира", дом="25", квартира="15")

mailing = Mailing(to_address=to_addr, from_address=from_addr, cost=450, track="TRK789012345")

print(f"Отправление {mailing.track} из {to_addr.индекс}, {to_addr.город}, {to_addr.улица}, {to_addr.дом} - {to_addr.квартира} в {from_addr.индекс}, {from_addr.город}, {from_addr.улица}, {from_addr.дом} - {from_addr.квартира}.")
print(f"Стоимость {mailing.cost} рублей.")
