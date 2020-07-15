

day = {
  'senin' : 'Monday',
  'selasa': 'Tuesday',
  'rabu' : 'Wednesday',
  'kamis' : 'Thusday',
  'jumat' : 'Friday',
  'Sabtu' : 'Saturday',
  'Minggu' : 'Sunday',
}

hari_list = list(day)
days_list = list(day.values())
print(hari_list)

inp = input('masukan nama hari :').lower
if inp in hari_list :
  day = days_list[hari_list.index(inp)]
  print('bahasa inggris dari', (inp), 'adalah', {day})
else :
  hari = hari_list[days_list.index(inp)]
  print('bahasa indonesia dari', (inp), 'adalah', {day})
