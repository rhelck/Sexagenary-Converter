print('''Please enter your date of birth below,
in a month, day, year format.
When prompted, answer whatever questions appear.
Use proper spelling.
Keep in mind that the Chinese New Year occurs about 
a month after the Western New Year. 
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
    'kong': '孔'
}
month_input = input('Month of birth: ').lower()
month_actual = month_input.split()
month_output = ' '
for month in month_actual:
    month_output += monthdict.get(month)
dayoutput = ''
day_input = input('Day of birth: ')
for day in day_input:
    if int(day_input) > 10:
        dayoutput += daydict.get(day)
        dayoutput1 = (dayoutput[:1] + '十' + dayoutput[1:])
    elif int(day_input) == 10:
        dayoutput1 = '十'
    else:
        dayoutput1 = daydict.get(day_input)
westyear = int(input('Year: '))
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
surname_input = input('Surname: ').lower()
surname_actual = surname_input.split()
for surname in surname_actual:
    surname_output = surnamedict.get(surname)
sex_input = input('Sex: ').lower()
if sex_input == 'man' or sex_input == 'male':
    sex_output = '男生'
elif sex_input == 'woman' or sex_input == 'female':
    sex_output = '女生'
print(f"姓氏{surname_output}, {sex_output}, 生日{stem_output}{branch_output}年, {month_output}月, {dayoutput1}日。")