import math

print('''Please enter your date of birth below,
in a month, day, year format.
When prompted, answer whatever questions appear.
Use proper spelling.
Keep in mind that the Chinese New Year occurs sometime in February. 
''')
monthdict = {
    'january':'一',
    'february':'二',
    'march':'三',
    'april':'四',
    'may':'五',
    'june':'六',
    'july':'七',
    'august':'八',
    'september':'九',
    'october':'十',
    'november':'十一',
    'december':'十二'
}
daydict = {
    '1':'一',
    '2':'二',
    '3':'三',
    '4':'四',
    '5':'五',
    '6':'六',
    '7':'七',
    '8':'八',
    '9':'九',
    '0':''
}
tendict = {
    '1':'',
    '2':'二',
    '3':'三',
    '4':'四',
    '5':'五',
    '6':'六',
    '7':'七',
    '8':'八',
    '9':'九',
    '0':''
}
yeardict1 = {
    '1':'甲',
    '2':'乙',
    '3':'丙',
    '4':'丁',
    '5':'戊',
    '6':'己',
    '7':'庚',
    '8':'辛',
    '9':'壬',
    '0':'癸'
}
yeardict2 = {
    '1':'子',
    '2':'丑',
    '3':'寅',
    '4':'卯',
    '5':'辰',
    '6':'巳',
    '7':'午',
    '8':'未',
    '9':'申',
    '10':'酉',
    '11':'戌',
    '0':'亥'
}
surnamedict = {
    'helck':'何',
    'smith':'匠',
    'peterson':'碑',
    'rigby':'坜',
    'lv':'吕',
    'qin': '秦',
    'meng': '孟',
    'mo': '墨',
    'lao': '老',
    'kong': '孔',
    'liu': '刘',
    'mi':'米'
}
try:
    def monthconverter(month_input):
        month_actual = month_input.split()
        month_output = ''
        for month in month_actual:
            month_output += monthdict.get(month)
        return(month_output)
    month_input = input('Month: ').lower()
    month_output = monthconverter(month_input)
except TypeError:
    print('Please input the full name of the month.')
    month_input = input('Month: ').lower()
    month_output = monthconverter(month_input)
#Days
try:
    dayinput = input('Day: ')
    ten_count = int(dayinput)//10
    single_count = int(dayinput)%10
    if int(dayinput) >= 10:
        single_output = daydict.get(str(single_count))
        ten_output = tendict.get(str(ten_count))
        dayoutput1 = (f"{ten_output}十{single_output}")
    elif int(dayinput) <10:
        single_output = daydict.get(str(dayinput))
        dayoutput1 = single_output
except ValueError:
    print('Please input the day of the month in numerical terms')
#This determines the lunar and lunisolar cycles.
westyear = int(input('Year: '))
solar_days = (westyear * 365.242189) + 7.8
synodic_period = solar_days % 29.530587981
first_new_moon = 29.530587981 - synodic_period
if first_new_moon < 21:
    unrifined_new_year = first_new_moon + 29.530587981
    if unrifined_new_year > 31:
        new_year = unrifined_new_year - 31
        month_of_new_year = 'february'
    elif unrifined_new_year <= 31:
        new_year = unrifined_new_year
        month_of_new_year = 'january'
elif first_new_moon >= 21:
    new_year = first_new_moon
    month_of_new_year = 'january'
#This determines whether the input is passed the Chinese New Year or not.
if month_of_new_year == 'january':
    if month_input == month_of_new_year:
        if int(dayinput) < new_year:
            westyear = westyear - 1
        elif int(dayinput) >= new_year:
            westyear = westyear
    elif month_input != month_of_new_year:
        westyear = westyear
elif month_of_new_year == 'february':
    if month_input == 'january':
        westyear = westyear - 1
    elif month_input == 'february':
        if int(dayinput) < new_year:
            westyear = westyear -1
        elif int(dayinput) >= new_year:
            westyear = westyear
truncated_new_year = math.trunc(new_year)
new_year_decimal = new_year - truncated_new_year
hour_count = new_year_decimal//(1/24)
#Year portion, main algorithim. Took a little while to create, but I'm very proud of it. First complex piece of code I have created entirely by myself.
era = input('Is this BC or AD? ').lower()
if era == 'ad':
    shortwestyear = westyear - 3
    divwestyear = shortwestyear//60
    remainder = shortwestyear-divwestyear*60
    component1 = remainder%10
    component2 = remainder%12        
elif era == 'bc':
    shortwestyear = westyear + 2
    divwestyear = shortwestyear//60
    remainder = shortwestyear-divwestyear*60
    antiremainder = 60 - remainder
    component1 = antiremainder%10
    component2 = antiremainder%12
stem_output = yeardict1.get(str(component1))
branch_output = yeardict2.get(str(component2))
#Names must be split, otherwise the dictionary malfunctions.
surname_input = input('Surname: ').lower()
surname_actual = surname_input.split()
for surname in surname_actual:
    surname_output = surnamedict.get(surname)
#Simple if-or statements for the gender portion.
sex_input = input('Sex: ').lower()
if sex_input == 'man' or sex_input == 'male':
    sex_output = '男生'
elif sex_input == 'woman' or sex_input == 'female':
    sex_output = '女生'
print(f"姓氏{surname_output}, {sex_output}, 生日{stem_output}{branch_output}年, {month_output}月, {dayoutput1}日 。")
print(f"New Year's Day is {month_of_new_year} {truncated_new_year}, at {hour_count} hours.")