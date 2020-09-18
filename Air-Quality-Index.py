import math 
#Christopher Pineda 2/29/20
#Project 1: A Breath of Fresh Air(Milestone 2)
'''
This program will ask the user to enter and name certain locations
the program will then ask the user to enter the pollutant amount for
various substances furthermore the program will print the AQI & the
quality of the air for every location and lastly the program will 
print the greates AQI out of all the locations and the average PM-2.5
concentration.
'''
#Variables
location_Amount = 0 
PM_25 = 0
PM_10 = 0
NO_2 = 0
SO_2 = 0 
CO = 0 
O_3 = 0 
max_AQI = 0 
overall_max = 0 
overall_max_location = ("location")
PM_25_Counter = 0 
PM_25_total = 0 

print("Air Quality Index Calculator")

#TODO check fot apporopriate truncations & round final AQI for every pollutant
#TODO find an average AQI for PM 2.5
#Do so by creating an acummaltor for pm 2.5 of every location, and a counting variable aswell 

# Will loop until user enters a location greater than 0 
while location_Amount <= 0 : 
    location_Amount = int(input("How many locations for this report? "))

    for i in range(1,location_Amount +1):

        max_AQI = 0 
        location_Name = str(input(f"What is the name of location {i}? "))

        PM_25 = float(input("-> Enter Pm- 2.5 concentration: "))
        PM_25 = (math.floor(PM_25 * 10)) /10
    
        if 500.4 >= PM_25 >= 250.5 : # Assaigns values to I High, I Low, C High, and C Low to the pollutant PM-2.5 depending on the users input
            I_high, I_low = 500, 301
            C_high, C_low = 500.4, 250.5
    
        elif 250.4 >= PM_25 >= 150.5 :
            I_high, I_low = 300, 201
            C_high, C_low = 250.4, 150.5
        
        elif 150.4 >= PM_25 >= 55.5 :
            I_high, I_low = 200, 151
            C_high, C_low = 150.4, 55.5
    
        elif 55.4 >= PM_25 >= 35.5 :
            I_high, I_low = 150, 101
            C_high, C_low = 55.4, 35.5
        
        elif 35.4 >= PM_25 >= 21.1 :
            I_high, I_low = 100, 51
            C_high, C_low = 35.4, 21.1
    
        elif  12.0 >= PM_25 >= 0:
            I_high, I_low = 50, 0
            C_high, C_low = 12.0, 0 

        if PM_25 >= 0 :
            AQI_PM_25 = round( ((I_high - I_low) / (C_high - C_low)) * (PM_25 - C_low) + I_low )
            print("PM-2.5 concentration of {} is index level {}".format(PM_25,AQI_PM_25))
            max_AQI = AQI_PM_25 # Setting max AQI to pollutant PM-2.5
            PM_25_total += PM_25
            PM_25_Counter += 1 
            

        PM_10 = float(input("-> Enter Pm-10 concentration: "))
        PM_10 = math.floor(PM_10)

        if 604 >= PM_10 >=425:
            I_high, I_low = 500, 301
            C_high, C_low = 604, 425
        
        elif 424 >= PM_10 >= 355:    
            I_high, I_low = 300, 201
            C_high, C_low = 424, 355

        elif 354 >= PM_10 >=255:
            I_high, I_low = 200, 151
            C_high, C_low = 354, 255

        elif 254 >= PM_10 >= 155:    
            I_high, I_low = 150, 101
            C_high, C_low = 254, 155 

        elif 154 >= PM_10 >=55:    
            I_high, I_low = 100, 51
            C_high, C_low = 154,  55

        elif 54 >= PM_10 >=0:    
            I_high, I_low = 50, 0
            C_high, C_low = 54, 0  

        if PM_10 >= 0 :
            AQI_PM_10 = round( ((I_high - I_low) / (C_high - C_low)) * (PM_10 - C_low) + I_low )
            print("PM-10 concentration of {} is index level {}".format(PM_10,AQI_PM_10))
            if max_AQI < AQI_PM_10 : # will assign max AQI to that of pollutant PM-10
                max_AQI = AQI_PM_10  # if the current max is less than PM-10 AQI 

        NO_2 = float(input("-> Enter NO-2 concentration: "))
        NO_2 = math.floor(NO_2)
        
        if 2049 >= NO_2 >= 1250 :
            I_high, I_low = 500, 301
            C_high, C_low = 2049, 1250
        
        elif 1249 >= NO_2 >= 650 :
            I_high, I_low = 300, 201
            C_high, C_low = 1249, 650
        
        elif 649 >= NO_2 >= 361 :
            I_high, I_low = 200, 151
            C_high, C_low = 649, 361
        
        elif 360 >= NO_2 >= 101:
            I_high, I_low = 150, 101
            C_high, C_low = 360, 101
        
        elif 100>= NO_2 >= 54 :
            I_high, I_low = 100, 51
            C_high, C_low = 100, 54
    
        elif 53 >= NO_2 >= 0 : 
            I_high, I_low = 50, 0 
            C_high, C_low = 53, 0 

        if  NO_2 >= 0 :
            AQI_NO_2 = round( ((I_high - I_low) / (C_high - C_low)) * (NO_2 - C_low) + I_low )
            print("NO-2 concentration of {} is index level {}".format(NO_2,AQI_NO_2))
            if max_AQI < AQI_NO_2 :
                max_AQI = AQI_NO_2

        SO_2 = float(input("-> Enter SO-2 concentration: "))
        SO_2 = math.floor(SO_2)

        if 1004 >= SO_2 >= 605 : 
            I_high, I_low = 500, 301
            C_high, C_low = 1004, 605

        elif 604 >= SO_2 >= 305 :
            I_high, I_low = 300, 201
            C_high, C_low = 604, 305

        elif 304 >= SO_2 >= 186 :
            I_high, I_low = 200, 151 
            C_high, C_low = 304,186

        elif 185 >= SO_2 >= 76 :
            I_high, I_low = 150, 101 
            C_high, C_low = 185, 76
       
        elif 75 >= SO_2 >= 36 :
            I_high, I_low = 100, 51
            C_high, C_low = 75, 36

        elif 35 >= SO_2 >= 0 :
            I_high, I_low = 50, 0
            C_high, C_low = 35, 0 
        
        if SO_2 >= 0 : 
            AQI_SO_2 = round( ((I_high - I_low) / (C_high - C_low)) * (SO_2 - C_low) + I_low )
            print("SO-2 concentration of {} is index level {}".format(SO_2,AQI_SO_2))
            if max_AQI < AQI_SO_2 :
                max_AQI = AQI_SO_2

        CO = float(input("-> Enter CO Concentration: "))
        CO = (math.floor(CO * 10)) /10

        if 50.4 >= CO >= 30.5 :
            I_high, I_low = 500,301
            C_high, C_low = 50.4, 30.5
    
        elif 30.4 >= CO >= 15.5 :
            I_high, I_low = 300, 201
            C_high, C_low = 30.4, 15.5
    
        elif 15.4 >= CO >= 12.5 : 
            I_high, I_low = 200, 151
            C_high, C_low = 15.4, 12.5
    
        elif 12.4 >= CO >= 9.5 : 
            I_high, I_low = 150, 101
            C_high, C_low = 12.4, 9.5
        
        elif 9.4 >= CO >= 4.5 :
            I_high, I_low = 100, 51
            C_high, C_low = 9.4, 4.5
    
        elif 4.4 >= CO >= 0 : 
            I_high, I_low = 50, 0
            C_high, C_low = 4.4, 0
        
        if CO >= 0 :
            AQI_CO = round ( ((I_high - I_low) / (C_high - C_low)) * (CO - C_low) + I_low )
            print("CO concentration of {} is index level {}".format(CO, AQI_CO))
            if max_AQI < AQI_CO :
                max_AQI = AQI_CO

        O_3 = float(input("-> Enter O3 concentration: "))
        O_3 = math.floor(O_3) 

        if 604 >= O_3 >= 405 :
            I_high, I_low = 500, 301
            C_high, C_low = 604, 405
        
        elif 404 >= O_3 >= 205 :
            I_high, I_low = 300, 201
            C_high, C_low = 404, 205
        
        elif 204 >= O_3 >= 165 :
            I_high, I_low = 200, 151
            C_high, C_low = 204, 165
        
        elif 164 >= O_3 >= 125 :
            I_high, I_low = 150, 101
            C_high, C_low = 164, 125
        
        if O_3 >= 125 :
            AQI_O_3 = round ( ((I_high - I_low) / (C_high - C_low)) * (O_3 - C_low) + I_low )
            print("O3 concentration of {} is index level {}".format(O_3,AQI_O_3))
            if max_AQI < AQI_O_3 :
                max_AQI = AQI_O_3
       
        if 500 >= max_AQI >= 301 : # These if statements compare max AQI to assign the qualtity of the air
            air_Quality = ("Hazardous")
        elif 300 >= max_AQI >= 201 :
            air_Quality = ("Very Unhealthy")
        elif 200 >= max_AQI >= 151 :
            air_Quality = ("Unhealthy")
        elif 150 >= max_AQI >= 101 :
            air_Quality = ("Unhealthy for sensitive groups")
        elif 100 >= max_AQI >= 51 :
            air_Quality = ("Moderate")
        else: 
            air_Quality = ("Good")

        print("AQI for {} is {} \nAir Quality: {}".format(location_Name,max_AQI,air_Quality)) #Printing the greatest AQI,Name of location, and the Air quality
         
        if overall_max <= max_AQI: # Checks for the largest AGI amongst all of the locations 
            overall_max = max_AQI 
            overall_max_location = location_Name

print("Summary: \nLocation with highest AQI is {} ({})".format(overall_max_location,overall_max)) 

if PM_25 > 0 :
    average_PM_25 = float(PM_25_total / PM_25_Counter) # This line of code calculates the average PM-2.5
    print("Average PM-2.5 concentration: {}".format(average_PM_25))
