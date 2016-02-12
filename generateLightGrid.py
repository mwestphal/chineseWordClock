import datetime
import lunardate

def getWeekDay(sd, lightGrid):
  weekday = sd.weekday();
  lightGrid += [(0,7)]; # xing 
  lightGrid += [(0,6)]; # qi

  if weekday == 0:
    # xing gi yi
    print("xing xi yi")
    lightGrid += [(0,5)];
  elif weekday == 1:
    # xing gi er
    print("xing xi er")
    lightGrid += [(0,4)];  
  elif weekday == 2:
    # xing gi san
    print("xing xi san")
    lightGrid += [(0,3)];
  elif weekday == 3:
    # xing gi si
    print("xing xi si")
    lightGrid += [(0,2)];
  elif weekday == 4:
    # xing gi wu
    print("xing xi wu")
    lightGrid += [(0,1)];
  elif weekday == 5:
    # xing gi lio
    print("xing xi lio")
    lightGrid += [(0,0)];
  else :
    # xing gi tian
    print("xing xi tian")
    lightGrid += [(1,7)];
  return

def getDayPeriod(sd, lightGrid):
  hour = sd.hour

  if hour >= 5 and hour < 8:
    # zhao shang
    print("zhao shang")
    lightGrid += [(1,6)];
    lightGrid += [(1,3)];
  elif hour >= 8 and hour < 11:
    # shang wu
    print("shang wu")
    lightGrid += [(1,3)];
    lightGrid += [(1,0)];
  elif hour >= 11 and hour < 13:
    # zhong wu
    print("zhong wu")
    lightGrid += [(1,2)];
    lightGrid += [(1,0)];
  elif hour >= 13 and hour < 18:
    # xia wu
    print("xia wu")
    lightGrid += [(1,1)];
    lightGrid += [(1,0)];
  elif hour >= 18 and hour < 23:
    # wan shang //TODO is it right end time ?
    print("wan shang")
    lightGrid += [(1,5)];
    lightGrid += [(1,3)];
  elif hour >= 23 or hour < 1:
    # wu ye 
    print("wu ye")
    lightGrid += [(1,0)];
    lightGrid += [(2,7)];
  else :
    # ye jian
    print("ye jian")
    lightGrid += [(2,7)];
    lightGrid += [(2,7)];
  return

def getHour(hour, lightGrid):
  if hour == 0:
    # shi er
    print("shi er")
    lightGrid += [(3,2)];
    lightGrid += [(3,0)];
  elif hour == 1:
    # yi
    print("yi")
    lightGrid += [(3,1)];
  elif hour == 2:
    # liang
    print("dian")
    lightGrid += [(4,4)];
  elif hour == 3:
    # san
    print("san")
    lightGrid += [(5,2)];
  elif hour == 4:
    # si
    print("si")
    lightGrid += [(5,7)];
  elif hour == 5:
    # wu
    print("wu")
    lightGrid += [(5,6)];
  elif hour == 6:
    # lio
    print("lio")
    lightGrid += [(5,5)];
  elif hour == 7:
    # ji
    print("ji")
    lightGrid += [(5,4)];
  elif hour == 8:
    # ba
    print("ba")
    lightGrid += [(5,3)];
  elif hour == 9:
    # jio
    print("jio")
    lightGrid += [(5,1)];
  elif hour == 10:
    # shi
    print("shi")
    lightGrid += [(3,2)];
  elif hour == 11:
    # shi yi
    print("shi yi")
    lightGrid += [(3,2)];
    lightGrid += [(3,1)];

  # dian
  print("dian")
  lightGrid += [(5,0)];
  return

def getTime(sd, lightGrid):
  hour = sd.hour%12
  minute = sd.minute

  if minute < 5 or ( minute >= 30 and minute < 35 ):
    getHour(hour, lightGrid);
    if minute >= 30:
      # ban
      print("ban")
      lightGrid += [(6,7)];
  
  elif minute <= 35:
    getHour(hour, lightGrid);
    
    if minute < 10:
      # ling wu fen
      print("ling wu fen")
      lightGrid += [(6,6)];
      lightGrid += [(7,6)];
      lightGrid += [(7,4)];
    elif minute < 15:
      # shi fen
      print("shi fen")
      lightGrid += [(7,7)];
      lightGrid += [(7,4)];
    elif minute < 20:
      # yi ke
      print("yi ke")
      lightGrid += [(6,3)];
      lightGrid += [(7,5)];
    elif minute < 25:
      # er shi fen
      print("er shi fen")
      lightGrid += [(6,2)];
      lightGrid += [(7,7)];
      lightGrid += [(7,4)];
    elif minute < 30:
      print("er shi wu fen")
      # er shi wu fen
      lightGrid += [(6,2)];
      lightGrid += [(7,7)];
      lightGrid += [(7,6)];
      lightGrid += [(7,4)];
    else:
      print("san shi wu fen")
      # san shi wu fen
      lightGrid += [(6,1)];
      lightGrid += [(7,7)];
      lightGrid += [(7,6)];
      lightGrid += [(7,4)];
  else:
    # cha
    print("cha")
    lightGrid += [(2,2)];
    if minute < 45:
      # er shi fen
      print("er shi fen")
      lightGrid += [(3,7)];
      lightGrid += [(3,6)];
      lightGrid += [(3,4)];
    elif minute < 50:
      # yi ke
      print("yi ke")
      lightGrid += [(2,1)];
      lightGrid += [(3,3)];
    elif minute < 55:
      # shi fen
      print("shi fen")
      lightGrid += [(3,6)];
      lightGrid += [(3,4)];
    elif minute <= 50:
      # wu fen
      print("wu fen")
      lightGrid += [(3,7)];
      lightGrid += [(3,4)];
    
    getHour((hour + 1)%12, lightGrid);
  return

def getMq(lightGrid):
  # mq
  lightGrid += [(7,3)]; 
  lightGrid += [(7,2)]; 
  return

def getYun(lightGrid):
  # yun
  lightGrid += [(7,0)]; 
  return

def getLove(lightGrid):
  # mq <3 yun
  getMq(lightGrid)
  lightGrid += [(7,1)]; 
  getYun(lightGrid)
  return

def getBirthday(lightGrid):
  # kuai le
  lightGrid += [(2,3)]; 
  lightGrid += [(6,5)]; 

def getHappy(lightGrid):
  # kuai le
  lightGrid += [(6,0)]; 
  lightGrid += [(6,4)]; 

def checkNewYear(sd, lightGrid):
  if sd.minute == 0:
    if sd.day == 1 and sd.month == 1:
      # xin nian
      lightGrid += [(1,5)]; 
      lightGrid += [(2,4)]; 
      getHappy(lightGrid);
      return True
  return False

def checkMqBirthday(sd, lightGrid):
  if sd.minute == 0:
    if sd.day == 17 and sd.month == 6:
      getBirthday(lightGrid);
      getHappy(lightGrid);
      getMq(lightGrid);
      return True
  return False

def checkYunBirthday(sd, lightGrid):
  if sd.minute == 0:
    if sd.day == 24 and sd.month == 6:
      getBirthday(lightGrid);
      getHappy(lightGrid);
      getYun(lightGrid);
      return True
  return False

def checkSpringFestival(sd, ld, lightGrid):
  if sd.minute == 0:
    if ld.day == 1 and ld.month == 1:
      # guo nian hao
      lightGrid += [(2,6)]; 
      lightGrid += [(2,4)]; 
      lightGrid += [(2,0)];
      return True
  return False

def checkLanternFestival(sd, ld, lightGrid):
  if sd.minute == 0:
    if ld.day == 15 and ld.month == 1:
      # yuan xiao jie
      lightGrid += [(4,6)]; 
      lightGrid += [(4,2)]; 
      lightGrid += [(4,0)];
      getHappy(lightGrid);
      return True
  return False

def checkMidAutumnFestival(sd, ld, lightGrid):
  if sd.minute == 0:
    if ld.day == 15 and ld.month == 8:
      # zhong qiu
      lightGrid += [(4,7)]; 
      lightGrid += [(4,5)]; 
      getHappy(lightGrid);
      return True
  return False

def checkValentineFestival(sd, ld, lightGrid):
  if sd.minute == 0:
    if ld.day == 7 and ld.month == 7:
      # xing ren jie
      lightGrid += [(4,3)]; 
      lightGrid += [(4,1)]; 
      lightGrid += [(4,0)]; 
      getHappy(lightGrid);
      return True
  return False

sd = datetime.datetime.now();
ld = lunardate.LunarDate.today();
lightGrid = [];

if checkNewYear(sd, lightGrid):
  print("NewYear")
elif checkMqBirthday(sd, lightGrid):
  print("mq")
elif checkYunBirthday(sd, lightGrid):
  print("yun")
elif checkSpringFestival(sd, ld, lightGrid):
  print("spring")
elif checkLanternFestival(sd, ld, lightGrid):
  print("lantern")
elif checkMidAutumnFestival(sd, ld, lightGrid):
  print("midautumn")
elif checkValentineFestival(sd, ld, lightGrid):
  print("valentine")
else:
  getWeekDay(sd, lightGrid);
  getDayPeriod(sd, lightGrid);
  getTime(sd, lightGrid);
  getLove(lightGrid);
print(sd)
print(lightGrid)


