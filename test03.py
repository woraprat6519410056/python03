#ให้ทำโปรแกรมป้อนจำนวนเงิน และจำนวนคนทางแป้นพิมพ์ และแสดงผลออกมาาว่า
#จำนวนเงิน ???? บาท จำนวนคน ???? คน ต้องหารกันคนละ ???? บาท
#ให้แสดงผลโดยใช้ print ทั้ง 5 แบบ
money = input('ป้อนจำนวนเงิน : ')
person = input('ป้อนจำนวนคน : ')
result = float(money) / int(person)
print('--------------------------')
print(f'จำนวนเงิน {float(money):.2f} บาท จำนวนคน {person} คน ต้องหารกันคนละ {(float(money)/int(person)):.2f}บาท')
print('จำนวนเงิน{:,.2f} บาท จำนวนคน {} ต้องหารคนละ {:,.2f} บาท' .format(float(money),person,result))
print('จำนวนเงิน ' +str(round(float(money)))+ ' บาท จำนวนคน ' +person+ ' คน ต้องหารกันคนละ ' +f'{result:.2f}'+ ' บาท ')
print('จำนวนเงิน', f'{float(money):,.2f}','บาท'," จำนวนคน" , person, ' ต้องหารกันคนละ',f'{result:.2f}',"บาท")
print('จำนวนเงิน %s บาท จำนวนคน %s คน ต้องหารกันคนละ %.2f บาท' %(f'{float(money):,.2f}',person,result))