#!/bin/bash
#allR="2.2 2.4"
#allx="100 300 1000 3000"
#allq="91 121 152 182"
#alli="CI CI_HQ CI_HQ_SD CI_SD CI_HQ_SDOL70 MG PC PC_CI_HQ_SDOL70 PC_CI_SD PC_CI_HQ_SD MG_PC_CI_HQ_SDOL70"

#echo $allR

for R in 2.4 
do
       rs=$(echo $R | awk '{print $1/2}')
       echo $rs  
	./CovidSim /NR:10 /c:16 /PP:preGB_R0=2.0.txt /P:p_NoInt.txt /CLP1:100000 /CLP2:0 /O:../../../MeanT16_NR10_GBmitigation/NoInt_R0=${R} /D:../population/GB_pop2018.bin /L:../population/NetworkGB_16T.bin /R:${rs} 98798150 729101 17389101 4797132
	for x in 100 300 1000 3000 
	do
           for q in 91 
           do
                   qo=$(echo $q | awk '{print $1+30}')
                   echo $q $qo
		   for i in PC CI CI_HQ CI_HQ_SD CI_SD CI_HQ_SDOL70 PC_CI_HQ_SDOL70
		   do
			  ./CovidSim /NR:10 /c:16 /PP:preGB_R0=2.0.txt /P:p_${i}.txt /CLP1:${x} /CLP2:${q} /CLP3:${qo} /CLP4:${qo} /O:../../../MeanT16_NR10_GBmitigation/${i}_${x}_${q}_R0=${R} /D:../population/GB_pop2018.bin /L:../population/NetworkGB_16T.bin /R:${rs} 98798150 729101 17389101 4797132
		   done
	   done
	done
done

