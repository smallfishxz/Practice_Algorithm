import heapq

def points_furthest(A,k):
  return sorted(A, key = lambda p: p[0]*p[0]+p[1]*p[1], reverse=True)[:k]

def points_furthest1(points,k):
  h=[]
  for i in range(0,k):
    x = points[i][0]
    y = points[i][1]
    d_n = x*x + y*y
    heapq.heappush(h, (d_n, points[i]))
  for i in range(k, len(points)):
    print(i, points[i])
    x = points[i][0]
    y = points[i][1]
    d_n = x*x + y*y
    x0 = h[0][1][0]
    y0 = h[0][1][1]
    d_h0 = x0*x0 + y0*y0
    if d_n > d_h0:
      heapq.heappushpop(h,(d_n, points[i]))
  return h

# O(nlogn)
def points_nearest(A,k):
  return sorted(A, key = lambda p: p[0]*p[0]+p[1]*p[1])[:k]

# O(n+klogn), space O(n)
def points_nearest2(points,k):
  h=[]
  for item in points:
    d = item[0]*item[0]+item[1]*item[1]
    heapq.heappush(h, (d, item))
  r=[]
  for i in range(k):
    r.append(heapq.heappop(h)[1])
  return r


ele_topk = points_furthest1([(0,10), (1,4), (2,3), (3,5), (4,12)],2)
print(ele_topk)
ele_lowk = points_nearest2([(0,10), (1,4), (2,3), (3,5), (4,12)],2)
print(ele_lowk)
  
  
