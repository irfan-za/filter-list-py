# soal no 3
# data=[1,2,-1,"budi"]

# def negatif(data):
#   """"fungsi filter angka negatif pada list. jika ada me-return true"""
#   hasil=False
#   for i in data:
#     if(type(i)== int):
#       if(i>0):
#         hasil=False
#       elif(i<0):
#         hasil=True
#   return hasil

# print(negatif(data))

# ============================================================
# soal no 4
# import shelve
file=open("cuaca.csv","r")
data_cuaca=file.readlines()

def bulan_negatif(months_data):
  months=[]
  for i in months_data:
    month_data=i.split(";")
    for j in month_data:
      # print(int(j))
      if "1" in j or "2" in j or "3" in j or "4" in j or "5" in j or "6" in j or "7" in j or "8" in j or "9" in j :
        if int(j)<0:
          months.append(month_data[1])
  months = list(dict.fromkeys(months))
  return(months)

# memanggil fungsi
print(bulan_negatif(data_cuaca))