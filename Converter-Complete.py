import math
before_new_year = False
print('''Please enter your date of birth below,
in a month, day, year format.
When prompted, answer whatever questions appear.
Use proper spelling.
Keep in mind that the Chinese New Year occurs sometime in February. 
''')
month_dictionary = {
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
day_dictionary = {
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
ten_dictionary = {
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
year_dictionary_1 = {
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
year_dictionary_2 = {
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
surname_dictionary = {
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
            month_output += month_dictionary.get(month)
        return(month_output)
    month_input = input('Month: ').lower()
    month_output = monthconverter(month_input)
except TypeError:
    print('Please input the full name of the month.')
    month_input = input('Month: ').lower()
    month_output = monthconverter(month_input)
#Days
try:
    def day_converter(dayinput):
        ten_count = int(dayinput)//10
        single_count = int(dayinput)%10
        if int(dayinput) >= 10:
            single_output = day_dictionary.get(str(single_count))
            ten_output = ten_dictionary.get(str(ten_count))
            dayoutput1 = (f"{ten_output}十{single_output}")
        elif int(dayinput) <10:
            single_output = day_dictionary.get(str(dayinput))
            dayoutput1 = single_output
        return (dayoutput1)
    dayinput = input('Day: ')
    day_result = day_converter(dayinput)
except ValueError:
    print('Please input the day of the month in numerical terms.')
    dayinput = input('Day: ')
    day_result = day_converter(dayinput)
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
            before_new_year = True
        elif int(dayinput) >= new_year:
            westyear = westyear
    elif month_input != month_of_new_year:
        westyear = westyear
elif month_of_new_year == 'february':
    if month_input == 'january':
        westyear = westyear - 1
        before_new_year = True
    elif month_input == 'february':
        if int(dayinput) < new_year:
            westyear = westyear -1
            before_new_year = True
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
elif era == 'bc' and before_new_year == False:
    shortwestyear = westyear + 2
    divwestyear = shortwestyear//60
    remainder = shortwestyear-divwestyear*60
    antiremainder = 60 - remainder
    component1 = antiremainder%10
    component2 = antiremainder%12
elif era == 'bc' and before_new_year == True:
    shortwestyear = westyear + 4
    divwestyear = shortwestyear//60
    remainder = shortwestyear-divwestyear*60
    antiremainder = 60 - remainder
    component1 = antiremainder%10
    component2 = antiremainder%12
stem_output = year_dictionary_1.get(str(component1))
branch_output = year_dictionary_2.get(str(component2))
#Names must be split, otherwise the dictionary malfunctions.
update_decision = input('Would you like to add a name to the dictionary? (Yes/No) ').lower()
if update_decision == 'yes':
    chinese_name = input('Chinese character: ')
    english_name = input('English name: ').lower()
    surname_dictionary.update({english_name : chinese_name})
elif update_decision == 'no':
    print('No name added')
surname_input = input('Surname: ').lower()
surname_actual = surname_input.split()
for surname in surname_actual:
    surname_output = surname_dictionary.get(surname)
#Simple if-or statements for the gender portion.
sex_input = input('Sex: ').lower()
if sex_input == 'man' or sex_input == 'male' or sex_input == 'm':
    sex_output = '男生'
elif sex_input == 'woman' or sex_input == 'female' or sex_input == 'f':
    sex_output = '女生'
elif sex_input == 'is good':
    sex_output = 'haha nice'
print(f"姓氏{surname_output}，{sex_output}，日期{stem_output}{branch_output}年， {month_output}月，{day_result}日。")
print(f"New Year's Day is {month_of_new_year} {truncated_new_year}, at {hour_count} hours.")
print("Please keep in mind that Chinese time is twelve hours ahead of the United States Eastern Time.")