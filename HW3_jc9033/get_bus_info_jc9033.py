import sys
import os
import numpy as np
import pandas as pd
import csv

url="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2]
BUS = pd.read_json(url)
try:
    ActiveBus = BUS['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
except:
    print("No Active Bus!")
    sys.exit(0)
ActiveBusNum = len(ActiveBus)

print("Bus Line:",sys.argv[2])
print("Number of Active Buses:",ActiveBusNum)
print("Latitude ,  Longitude , Stop Name , Stop Status")

csvoutput = ["Latitude" ,  "Longitude" , "Stop Name" , "Stop Status" ]
with open("busline.csv","w") as csvfile: 
    writer = csv.writer(csvfile)
    writer.writerow(csvoutput)
    csvfile.close()
    
for i in range(ActiveBusNum):
    location = ActiveBus[i]['MonitoredVehicleJourney']['VehicleLocation']
    try:
        StopName = ActiveBus[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][1]['StopPointName']
        StopStatus = ActiveBus[i]['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['PresentableDistance']
    except:
        StopStatus = "N/A"
        StopName = "N/A"
    print("%.6f" % location['Latitude'] ,",", "%.6f" % location['Longitude'] ,",", StopName ,",", StopStatus)      
    csvoutput=(["%.6f" % location['Latitude'] , "%.6f" % location['Longitude'] , StopName , StopStatus])
    with open("busline.csv","a") as csvfile: 
        writer = csv.writer(csvfile)
        writer.writerow(csvoutput)
        csvfile.close()   

os.rename("busline.csv", sys.argv[3])