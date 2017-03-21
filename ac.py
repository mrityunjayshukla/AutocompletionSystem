import sys
import redis
r = redis.StrictRedis(host=<your ElastiCache endpoint DNS>..cache.amazonaws.com', port=6379, db=0)
def complete(r,prefix,count):
  results = []
  grab = 42
  start = r.zrank('autocomplete',prefix)
  if not start:
    return []
  while (len(results) != count):
    range = r.zrange('autocomplete',start,start+grab-1)
    start += grab
    if not range or len(range) == 0:
      break
    for entry in range:
      minlen = min(len(entry),len(prefix))
      if entry[0:minlen] != prefix[0:minlen]:
        count = len(results)
        break
      if entry[-1] == "%" and len(results) != count:
        results.append(entry[0:-1])
  return results

def autoComplete():
  print complete(r,sys.argv[1],50)

if __name__ == "__main__":
  autoComplete()
