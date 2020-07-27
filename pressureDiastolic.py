sist = int(input("Sistólica: "))
diast = int(input("Diastolic: "))

if sist >= 180 or diast >= 120:
    print("Crise hipert.")
elif (sist >= 140 and sist < 180) or (diast >= 90 and diast < 120):
    print("Hipertensão est. 2")
elif (sist >= 130 and sist <= 139) or (diast >= 80 and diast <= 89):
    print("Hipertensão est. 1")
elif (sist >= 80 and sist <= 70) or (diast >= 70 and diast <=50):
    print("Normal")