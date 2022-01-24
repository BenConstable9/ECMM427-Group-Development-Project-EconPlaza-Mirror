if [[ -z $1 ]]
then
  echo "Task Definition Required"
  exit 1
fi

while [[ true ]]
do
    $state=$(curl -s http://192.168.0.15:9999/blue-green-state/$1)
    echo $state
  if [[ $state == Done* ]]
  then
    exit 0
  fi
  if [[ $state == Fail* ]]
  then
    exit 1
  fi
  sleep 5
done