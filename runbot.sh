# Set nohup to 1 to write to nohup
nohup=0

if [[ -f nohup.out ]]
then 
    rm nohup.out
fi

if [ $nohup == 1 ]
then
    nohup ./run_tracker.sh &
else
    nohup ./run_tracker.sh </dev/null >/dev/null 2>&1 &
fi