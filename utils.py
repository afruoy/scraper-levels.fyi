df_columns = ["Job", "Company", "Country", "Region", "City", 
            "Date", "Level", "Tag", "Years Comp", 
            "Years Xp", "Compensation", "Base", 
            "Stock", "Bonus", "Nego Gain"]


def format_salary(s):
    if '$' in s:
        return int(s.split(',')[0][1:])
    if "N" in s:
        return 0
    return int(float(s[:-1]))


def format_date(d):    
    revers = d.split("/")[::-1]
    return revers[0] + "/" + revers[1] + "/" + revers[2]
    

