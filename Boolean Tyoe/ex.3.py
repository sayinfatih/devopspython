daily_calory = 1700
running_distance = 3
walking_steps = 4000

is_calory = daily_calory < 1500
is_runnig = running_distance >= 4
is_steps = walking_steps >=10000

can_loose_weight = (is_calory or is_runnig) and is_steps
print(can_loose_weight)