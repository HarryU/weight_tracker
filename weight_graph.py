from datetime import datetime, timedelta
from matplotlib import pyplot as plt
import matplotlib.dates as mdates

target_weight = 168.0
weekly_loss_target = 1.5

date_strings = ['05/02/2017', '12/02/2017', '19/02/2017', '26/02/2017', '05/03/2017', '12/03/2017', '19/03/2017', '26/03/2017', '01/04/2017', '09/04/2017']

dates = [datetime.strptime(d, '%d/%m/%Y').date() for d in date_strings]
weights = [215.6, 210.0, 209.8, 207.8, 208.2, 206.8, 202.8, 201.0, 201.6, 201.8]
target_weights = [weights[0]]
while target_weights[-1] > target_weight:
    target_weights.append(target_weights[-1] - weekly_loss_target)
target_dates = [dates[0] + timedelta(days=7*i) for i in range(len(target_weights))]
#target_weights = [weights[0] - (weekly_loss_target * i) for i in range(len(dates))]
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
plt.gca().xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.SU))

plt.plot(dates, weights)
plt.plot(target_dates, target_weights)
plt.gcf().autofmt_xdate()
plt.show()

