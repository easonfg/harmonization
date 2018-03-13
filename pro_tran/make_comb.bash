for i in 0 1 2 3 4 5 6 7 8 9
  do
    file='trainv_'$i'_comb_proTran'
    if [ -f $file ] ; then
      rm $file
    fi
    for j in 1 2 3
      do
        tail -n +2 'trainv_'$i'_'$j'_trained_m_reduced_100_proTran' >> 'trainv_'$i'_comb_proTran'
      done
    num_line=$(wc -l < 'trainv_'$i'_comb_proTran')
    num_word=$(head -n 1 'trainv_'$i'_comb_proTran' | wc -w)
    num_word=$((num_word-1))
    echo $num_line $num_word | cat - 'trainv_'$i'_comb_proTran' > temp && mv temp 'trainv_'$i'_comb_proTran'
  done

        #num_line=$(wc -l < 'trainv_0_comb')
        #num_word=$(head -n 1 'trainv_0_comb' | wc -w)
