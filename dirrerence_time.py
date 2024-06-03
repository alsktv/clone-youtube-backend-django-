from django.utils import timezone


#언제 전에 컨탠츠가 생성됬는지 나타내주는 함수
def TimeDifference(created_at):
    now = now = timezone.now()
    time = (now - created_at).total_seconds() #시간 차이   #초단위로 나옴, 필요에 따라 변형해주기.

    if(time/60 < 60):
      return  f"{int(time//60)}분전"
    elif(time/3600 < 24):
       return  f"{int(time//3600)}시간전"
    elif((time/3600) // 24 < 30):
       return f"{int((time//3600)//24 )}일전"
    elif((time//3600)//24//30 < 12):
       return  f"{int((time//3600)//24//30 )}달전"
    else:
       return  f"{int((time//3600)//24//30//12) }년전"