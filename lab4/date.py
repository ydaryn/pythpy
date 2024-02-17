#ex1
from datetime import datetime, timedelta
current_date = datetime.now()
five_days_ago = current_date - timedelta(days=5)
print(five_days_ago.strftime("%Y.%m.%d"))

#ex2
from datetime import datetime, timedelta
today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow=today + timedelta(days=1)
print(yesterday.strftime("%Y.%m.%d"))
print(today.strftime("%Y.%m.%d"))
print(tomorrow.strftime("%Y.%m.%d"))

#ex3
from datetime import datetime
seichas = datetime.now()
bez_micro = seichas.replace(microsecond=0)
print(bez_micro)

#ex4
from datetime import datetime
date1_str=input()
date2_str=input()
date1=datetime.strptime(date1_str, "%d.%m.%Y")
date2=datetime.strptime(date2_str, "%d.%m.%Y")
diff=abs((date1-date2).total_seconds())
print(diff)