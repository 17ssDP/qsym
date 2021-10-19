wdir=$1
logs=`find ${wdir} -name pin.log`
total_branch=0
unsat_branch=0
optimictic_branch=0
testcases=0
for log in ${logs} 
do
    unsat=`cat $log | grep "unsat" | wc -l`
    optimistic=`cat $log | grep "optimistic" | wc -l`
    testcase=`cat $log | grep "New testcase" | wc -l`
    ((unsat_branch=$unsat_branch+$unsat))
    ((optimistic_branch=$optimistic_branch+$optimistic))
    ((testcases=$testcases+$testcase))
done
((unsat_branch=$unsat_branch-$optimistic_branch))
((total_branch=$testcases+$unsat_branch))
echo "total branch = $total_branch"
echo "unsat branch = $unsat_branch"
echo "optimistic branch = $optimistic_branch"
echo "testcases = $testcases"