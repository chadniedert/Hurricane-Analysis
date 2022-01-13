# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}
def update_damages():
  damages_new = []
  for damage in damages:
    if damage[0] != "D":
      damages_new.append(float(damage[:-1]) * conversion[damage[-1]])
    else: 
      damages_new.append("Damages not recorded")
  return damages_new

# Test function by updating damages
damages = update_damages()
#print(damages)

# Create and view the hurricanes dictionary
hurricanes = {}
for i in range(len(names)):
  hurricanes[names[i]] = {"Names" : names[i], "Month": months[i], "Year" : years[i], "Max Sustained Wind" : max_sustained_winds[i], "Areas Affected" : areas_affected[i], "Damage" : damages[i], "Deaths": deaths[i]}
#print(hurricanes)

# Create a new dictionary of hurricanes with year and key
hurricanes_year_key = {}
for i in range(len(years)):
  hurricanes_year_key[years[i]] = hurricanes[names[i]]
#print(hurricanes_year_key)

# Create dictionary of areas to store the number of hurricanes involved in
locations_no_removals = []
for area in areas_affected:
  for each in area:
    locations_no_removals.append(each)
locations_no_dups = []
for loc in locations_no_removals:
  if loc not in locations_no_dups:
    locations_no_dups.append(loc)
location_counts = []
for loc in locations_no_dups:
  location_counts.append(locations_no_removals.count(loc))
affected_area_counts = {}
for i in range(len(locations_no_dups)):
  affected_area_counts[locations_no_dups[i]] = location_counts[i] 
#print(affected_area_counts)

# Calculating Maximum Hurricane Count
# find most frequently affected area and the number of hurricanes involved in
def area_affected_most():
  conv_list = list(affected_area_counts);
  return conv_list[0]
#print(area_affected_most())

# Calculating the Deadliest Hurricane
# find highest mortality hurricane and the number of deaths
def max_deaths():
  cane_name = ""
  max_death_count = 0
  for k, v in list(zip(names, deaths)):
    if v > max_death_count:
      max_death_count = v
      cane_name = k
  print("Cane with max deaths -> " + cane_name + "\nNumber of deaths -> " + str(max_death_count))

# Rating Hurricanes by Mortality
# categorize hurricanes in new dictionary with mortality severity as key
hurricanes_by_mortality = {0: [], 1: [], 2: [], 3: [], 4: []}

for i in range(len(names)):
  if deaths[i] > 10000:
    hurricanes_by_mortality[4].append(names[i])
  elif deaths[i] > 1000:
    hurricanes_by_mortality[3].append(names[i])
  elif deaths[i] > 500:
    hurricanes_by_mortality[2].append(names[i])
  elif deaths[i] > 100:
    hurricanes_by_mortality[1].append(names[i])
  else:
    hurricanes_by_mortality[0].append(names[i])
#print(hurricanes_by_mortality)
    
# Calculating Hurricane Maximum Damage
# find highest damage inducing hurricane and its total cost
max_cost = 0
for damage in damages:
 if damage != "Damages not recorded" and damage > max_cost:
   max_cost = damage
print(names[damages.index(max_cost)])

# Rating Hurricanes by Damage
# categorize hurricanes in new dictionary with damage severity as key
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
for i in range(len(names)):
  if damages[i] != "Damages not recorded" and damages[i] > damage_scale[4]:
    hurricanes_by_damage[5].append(names[i])
  elif damages[i] != "Damages not recorded" and damages[i] > damage_scale[3]:
    hurricanes_by_damage[4].append(names[i])
  elif damages[i] != "Damages not recorded" and damages[i] > damage_scale[2]:
    hurricanes_by_damage[3].append(names[i])
  elif damages[i] != "Damages not recorded" and damages[i] > damage_scale[1]:
    hurricanes_by_damage[2].append(names[i])
  elif damages[i] != "Damages not recorded" and damages[i] > damage_scale[0]:
    hurricanes_by_damage[1].append(names[i])
  else:
    hurricanes_by_damage[0].append(names[i])
print(hurricanes_by_damage)
