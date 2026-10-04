f=$1
tr -d '\n' <$f | wc -c
sed 's/3\*v/N*v/;s/c\/3/c\/N/;s/c%3/c%N/;s/int\*\*P/int N,**P/;s/;}\([a-zA-Z]\)(/;}\n\1(/g;s/;\([A-Za-z]\)(i,I/;\n\1(i,I/;s/;}main(/;}\nmain(/' $f > W.c && timeout 150 bash check8.sh W.c 2>&1|tail -2
for n in 1 2; do sed "s/3\*v/$n*v/;s/c\/3/c\/$n/;s/c%3/c%$n/" $f > w.c; gcc -w -fsanitize=address,undefined w.c -o w && echo "N=$n -> $(timeout 60 ./w 2>&1|head -2)"; done
gcc -w -fsanitize=address,undefined $f -o s && timeout 10 ./s; echo "TREE3 asan rc=$? (124 ok)"
