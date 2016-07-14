#!/bin/bash

if [ $# != 1 ]
then
	echo "args error"
	exit 1
fi

for pid in $(ps x|grep $1|grep -v "grep\|kill"|awk '{print $1}');do
	echo $pid
	kill $pid
done
