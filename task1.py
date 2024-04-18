import urllib.request as request
import json
import csv


merge_data=[]

merge_dict={}
merge_list=[]
with request.urlopen("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2") as response2:
    data2=json.load(response2)["data"]
with request.urlopen("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1") as response:
    data=json.load(response)["data"]["results"]
    for n2 in data2:
        ser2=n2["SERIAL_NO"]
        for n1 in data:
            if n1["SERIAL_NO"]==ser2:
                merge={**n2,**n1}
                merge_data.append(merge)
with open("spot.csv","w",newline="",encoding="utf-8") as file:
    data1=csv.writer(file)
    for location in merge_data:
        index=location["filelist"].lower().find(".jpg")
        imageurl=location["filelist"][:index+4]
        addre=location["address"][5:8]
        data1.writerow([location["stitle"],addre,location["longitude"],location["latitude"],imageurl])
    for location in merge_data:
        n=location["MRT"]
        m=location["stitle"]
        x=[n,m]
        merge_list.append(x)
    for station, attraction in merge_list:
        if station in merge_dict:
            merge_dict[station].append(attraction)
        else:
            merge_dict[station]=[attraction]
    merge_result=[[station]+attraction for station, attraction in merge_dict.items()]
with open("mrt.csv","w",newline="",encoding="utf-8") as file:
    data2=csv.writer(file)
    for n in merge_result:
        data2.writerow(n)