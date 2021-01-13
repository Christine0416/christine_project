#!/bin/bash

for R in 2.5 3.0 3.5 4.0 
do
       rs=$(echo $R | awk '{print $1/2}')
       echo $rs  
	./covid-sim/CovidSim /NR:10 /c:16 /A:covid-sim/data/admin_units/United_Kingdom_admin.txt /PP:preUK_R0=2.0.txt /P:p_NoInt.txt /CLP1:100000 /CLP2:0 /O:MeanT16_NR10/NoInt_cal1_R0=${R} /D:wpop_eur.txt /R:${rs} 98798150 729101 17389101 4797132
		   for i in PC_CI_HQ_SD
		   do
			  ./covid-sim/CovidSim /NR:10 /c:16 /A:covid-sim/data/admin_units/United_Kingdom_admin.txt /PP:preUK_R0=2.0.txt /P:p_${i}.txt /CLP1:${x} /CLP2:${q} /CLP3:${qo} /CLP4:${qo} /O:MeanT16_NR10/${i}_cal1_R0=${R} /D:wpop_eur.txt /R:${rs} 98798150 729101 17389101 4797132
		   done
	   done
	done
done

