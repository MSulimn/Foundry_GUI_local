

def calculate_pouring(volume,flowrate):
    volume_crucible = 100 # Current crucible volume
    volume_max = 2411000  # Max Volume crucible can contain
    volume_min = 100000   # Min volume crucible can contain
    max_tr = 2.5          # Max rise time
    min_tr = 1.5          # Min rise time

    # Condition for checking if the current crucible volume is sufficient 
    if(volume > volume_crucible): 
        
      
        volume_mean = ((volume_max + volume_min) / 2) 

        # checking wether the provided volume is in the lower or the upper part of our boundries
        if(volume >= volume_min and volume <= volume_mean):
             Tst = (volume/flowrate) - (2*min_tr) 
        elif(volume >= volume_mean and volume <= volume_max):
             Tst = (volume/flowrate) - (2*max_tr) 
   
        return round(Tst,1)

    
    else: print("Not enough material")



def get_degassing_time(time_last_melted,volume):
    '''
    Deriving a linear equation as a function of volume to get time 
    
    '''
    volume_max = 2411000

    max_t = 15

    min_t = 2

    volume_min = (min_t*volume_max)/max_t

    m = (max_t-min_t)/(volume_max-volume_min)
   
    b = max_t - m*volume_max
  
    time = m*volume + b 

    return round(time,1)


# shorter time_last_melted  == less time required
# Might be needed later 
    




