# Quite similar to the max # of points in point_intervals algorithm. 
# Create a tmp list of tuple (timepoint, 1/-1): all time points for the start/end time of meetings, and 1 for start
# time, and -1 for end time
# Then sort this tmp list with key (timepoint, and -1/1). Note: this is different from the max # of points, that is, it considers the end time first, and then the start time. 

def meeting_room(timeslots):
  timepoints = []
  for slot in timeslots:
    timepoints.append((slot[0], 1))
    timepoints.append((slot[1],-1))
  
  timepoints.sort(key = lambda point: (point[0], point[1]))
  
  max_r = -1
  max_p = None
  s = 0
  
  for point in timepoints:
    s += point[1]
    if s > max_r:
      max_r = s
      max_p = point[0]
  
  return(max_r, max_p)
  
print(meeting_room([[1000, 1030],[1000, 1100],[1030, 1130],[1100, 1200], [1300, 1400]]))
  
