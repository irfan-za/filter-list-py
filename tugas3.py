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
bulan=[]

def bulan_negatif(data):
  for i in data:
    data_per_bulan=i.split(";")
    for j in data_per_bulan:
      # print(int(j))
      if "1" in j or "2" in j or "3" in j or "4" in j or "5" in j or "6" in j or "7" in j or "8" in j or "9" in j :
        if int(j)<0:
          bulan.append(data_per_bulan[1])
  return(bulan)

# memanggil fungsi
print(bulan_negatif(data_cuaca))