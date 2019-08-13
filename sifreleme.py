print("Programa hoşgeldin.")
sifre=input("Lütfen parolayı giriniz.\n")
__import__("os").system("cls")

if sifre=="123": 
	print("Parolayı doğru girdiniz.")
	input('Bilgilere erişmek için "Enter" tuşuna basınız.\n')
	__import__("os").system("cls")
	print("ILHAN_AKIN isimli modemin şifresi: ilhan2005")
	girilensifre = "dogru"
	input()


else:
	print("Şifreyi yanlış girdiniz.")
	girilensifre="yanlis"


if girilensifre == "yanlis": 

	sifre=input("Lütfen parolayı tekrardan giriniz.\n")
	__import__("os").system("cls")

	if sifre=="123": 
		print("Parolayı doğru girdiniz.")
		input('Bilgilere erişmek için "Enter" basınız.\n')
		__import__("os").system("cls")
		print("ILHAN_AKIN isimli modemin şifresi: ilhan2005")
		input()

	else:
		print("Şifreyi yanlış girdiniz.")
		print('Programı kapatmak için "Enter" tuşuna basınız.')
		input()