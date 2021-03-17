# Part. 1
#=======================
# Import module
# csv -- fileIO operation
import csv
#=====================
# Part. 2
# Read cwb weather data
cwb_filename = '107030031.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
    mycsv = csv.DictReader(csvfile)
    header = mycsv.fieldnames
    for row in mycsv:
        data.append(row)
#===================
# Part. 3
# Analyze data depend on your group and store it to target_data like:
# Retrieve all data points which station id is "C0X260" as a list.
# target_data = list(filter(Lambda item: item['station_id'] == 'C0X260', data))

target_data = list(filter(lambda item: item['HUMD'] != '-99.000', data))
target_data1 = list(filter(lambda item: item['station_id'] == 'C0A880', target_data))
target_data2 = list(filter(lambda item: item['station_id'] == 'C0F9A0', target_data))
target_data3 = list(filter(lambda item: item['station_id'] == 'C0G640', target_data))
target_data4 = list(filter(lambda item: item['station_id'] == 'C0R190', target_data))
target_data5 = list(filter(lambda item: item['station_id'] == 'C0X260', target_data))

GetHUMD = lambda index,dataIn: [column[index] for column in dataIn if index in column]

final_data1 = map (float, GetHUMD('HUMD', target_data1))
final_data_1 = list (final_data1)
sum1 = sum (final_data_1)
if sum1==0: 
    sum1 = 'None'

final_data2 = map (float, GetHUMD('HUMD', target_data2))
final_data_2 = list (final_data2)
sum2 = sum (final_data_2)
if sum2==0: 
    sum2 = 'None'

final_data3 = map (float, GetHUMD('HUMD', target_data3))
final_data_3 = list (final_data3)
sum3 = sum (final_data_3)
if sum3==0: 
    sum3 = 'None'

final_data4 = map (float, GetHUMD('HUMD', target_data4))
final_data_4 = list (final_data4)
sum4 = sum (final_data_4)
if sum4==0: 
    sum4 = 'None'
    
final_data5 = map (float, GetHUMD('HUMD', target_data5))
final_data_5 = list (final_data5)
sum5 = sum (final_data_5)
if sum5==0: 
    sum5 = 'None'
#===========================
# Part. 4
# Print result
#print (target_data4)
#print (final_data3)

print (['C0A880', sum1], ['C0F9A0', sum2], ['C0G640', sum3], ['C0R190', sum4], ['C0X260', sum5])

#==============================