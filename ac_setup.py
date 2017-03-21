import redis
r = redis.StrictRedis(host='<your ElastiCache endpoint DNS>', port=6379, db=0)
f = open(‘autocomplete.txt',"r")
  for line in f:
    n = line.strip()
    for l in range(1,len(n)):
      prefix = n[0:l]
      r.zadd('autocomplete',0,prefix)
    r.zadd('autocomplete',0,n+"%")
else:
  exit
