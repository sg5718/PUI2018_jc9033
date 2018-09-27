import sys
url="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=" +sys.argv[2]
import pandas as pd
BUS = pd.read_json(url)
try:
    ActiveBus = BUS['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
except:
    print("No Active Bus!")
    sys.exit(0)
ActiveBusNum = len(ActiveBus)
print("Bus Line:",sys.argv[2])
print("Number of Active Buses:",ActiveBusNum)
for i in range(ActiveBusNum):
    location = ActiveBus[i]['MonitoredVehicleJourney']['VehicleLocation']
    print('Bus', i ,'is at latitude', "%.6f" % location['Latitude'] , 'and longitude' , "%.6f" % location['Longitude'])