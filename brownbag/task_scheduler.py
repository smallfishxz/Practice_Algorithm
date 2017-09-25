# We have a list of various types of tasks to perform. 
# Task types are identified with an integral identifier: task of type 1, task of type 2, task of type 3, etc. 
# Each task takes 1 time slot to execute, and once we have executed a task we need cooldown (parameter) time slots to recover 
# before we can execute another task of the same type.  
# However, we can execute tasks of other types in the meantime.  The recovery interval is the same for all task types. 
# We do not reorder the tasks: always execute in order in which we received them on input. 

# Given a list of input tasks to run, and the cooldown interval, output the minimum number of time slots required to run them.

# time complexity: O(N)
# space: O(num_task_type)
def schedule_task(task_in, cooldown):
  # initialize the required time slot as 0, and a dictionary to record the slot number
  # that a type of task was last executed
  pos = 0
  last_execution = dict()
  for task in task_in:
    # if the task is scheduled for the first time, directly put into the scheduler
    # and update the dictionary
    if task not in last_execution:
      pos += 1
      last_execution[task] = pos
      print(last_execution)
    # if the task has been executed before
    else:
      # since_last gets how many slots have been past since last execution
      since_last = pos - last_execution[task]
      # wait to get how many more slots needed to wait
      wait = cooldown - since_last
      # pos is updated to reflect which slot this task could be inserted
      pos += wait+1
      # update dictionary to reflect the new last execution slot
      last_execution[task] = pos
      print(last_execution)
  return pos

# This solution can be optimized to use memory O(min(num_task_type, cooldown_time)).
# Iterate over entire hash map every cooldown steps and delete unneeded entries
# Time complexity is still O(N)

def schedule_task1(task_in, cooldown):
  pos = 0
  last_execution = dict()
  for i in range(len(task_in)):
    task = task_in[i]
    if task not in last_execution:
      pos+=1
      last_execution[task]=pos
    else:
      since_last = pos - last_execution[task]
      wait_time = cooldown - since_last
      pos += wait_time + 1
      last_execution[task] = pos
    # Optimization
    if i % cooldown == 0:
      to_remove = []
      for tas, etime in last_execution.items():
        if cooldown < pos - etime:
          to_remove.append(tas)
      for tas in to_remove:
        del last_execution[task]
  return pos
  
print(schedule_task([1,1,2,1], 2))
print(schedule_task([1,2,3,1,2,3], 3))
print(schedule_task1([1,2,3,4,5,6,2,4,6,1,2,4], 6))
