def convert():
    ts = raw_input().strip()
    am_pm = ts[-2:]
    hr = ts[:2]
    
    if hr =='12':
        if am_pm == 'AM':
            print '00'+ ts[2:-2]
            
        elif am_pm == 'PM':
            print '12'+ ts[2:-2]
            
    
    elif am_pm == 'PM':
        int_hr = int(hr)
        mil_hr = int_hr +12
        mil_time = str(mil_hr) + ts[2:-2]
        print mil_time
        

    else:
        mil_time = ts[:-2]
        print mil_time
        
convert()