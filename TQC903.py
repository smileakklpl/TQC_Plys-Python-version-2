with open("data.txt","a+",encoding="utf-8") as file:
    for i in range(5):
        file.write("\n"+input())
    print("Append completed!")
    print("Content of \"data.txt\":")
    file.seek(0)
    print(file.read())
    
#a+從屁股開始寫
#file.seek()移動指標