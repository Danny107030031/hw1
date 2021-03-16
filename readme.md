1. First we need a csv file. By changing `cwb_filename = '107030031.csv'`, we can read different data.

2. After reading the data, we then need to remove the data whose value is -99.000 or -999.000. The function `filter` can help us achieve this.

3. After the values are removed, we use `filter` again to get all the information from the five stations .

4. The following line `GetHUMD = lambda index,dataIn: [column[index] for column in dataIn if index in column]` is the key to extracting humidity values.

5. By using functions `map` and `float`, we convert all the hunidity values into float data type since they were saved as string.

6. Finally, we use the function `sum` to get the summation of humidity values.

7. The results are shown as below. `['C0A880', 20.359999999999996] ['C0F9A0', 16.35] ['C0G640', 18.709999999999997] ['C0R190', 16.62] ['C0X260', 19.05]
]`