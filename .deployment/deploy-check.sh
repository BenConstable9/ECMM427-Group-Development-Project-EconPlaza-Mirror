if [ -z $1 ]
then
  echo "Task Definition Required"
  exit 1
fi

count=0
while [ true ]
do
  count=$((count+1))
  state=$(curl -s http://192.168.0.15:9999/blue-green-state/$1)
  echo "$state"
  if test "${state##Done*}" = ""
  then
    exit 0
  fi
  if test "${state##Fail*}" = ""
  then
    exit 1
  fi
  if [ $count -gt 600 ]
  then
    echo "Timeout Failure: Deployment took too long"
    exit 1
  fi
  sleep 5
done