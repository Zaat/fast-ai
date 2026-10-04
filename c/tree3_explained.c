/* tree3_explained.c - the 545-char tree3.c with line breaks and comments.
   Same tokens, same behaviour. Build: gcc -w tree3_explained.c (gcc, x86-64).

   Tree layout (preorder, one int array of length 2n for an n-node tree):
     t[i]   = end of node i's subtree (exclusive), so t[0] = n
     t[n+i] = colour of node i (0..2)
   Children of node i: i+1, then t[i+1], ... while < t[i].
   A used child is marked by negating its end value. */

int **P,   /* all generated trees, sorted by size; P[0] is an empty seed tree */
    **S,   /* S[d] = d-th tree of the current sequence */
    p=1,   /* number of trees in P */
    q,k,i,c,j,
    M,     /* longest sequence found (TREE(3) when the search ends) */
    *x,*y; /* the two trees being compared (globals: never change during one check) */

/* F: can the x sibling subtrees starting at i (up to I) each be placed into a
   *different* y subtree within [j,J)?  x subtree i "fits" in y subtree c if some
   node n inside c has the same colour and n's children can take i's children. */
F(i,I,j,J){
  int c=j,n=j,r=i/I;            /* r=1 when no x subtrees are left (i==I) */
  for(;n<J>r;n++)               /* (n<J)>r: keep going while n<J and not done */
    n<abs(y[c])||(c=n),         /* c = the child subtree that contains n */
    n<y[c]&&                    /* skip subtrees already used (negative end) */
    x[*x+i]==y[*y+n]&           /* colours match ... */
    F(i+1,x[i],n+1,y[n])&&      /* ... and children fit */
    (y[c]*=-1,r=F(x[i],I,j,J),y[c]*=-1); /* mark c, place the remaining x siblings, unmark */
  return r;
}

/* g(v): build every 3-coloured tree with v nodes from the (v-1)-node trees at the
   end of P, by inserting a new node at position i (as first child of node i-1;
   position 0 = new root above everything, used to build the single-node trees). */
g(v){
  for(S=realloc(S,8*p),k=p;k&&*(x=P[--k])+1==v;)
    for(c=3*v;c--;)             /* i = position, c%3 = colour of the new node */
      for(i=c/3,P=realloc(P,8*p+8),P[p++]=y=realloc(0,8*v),j=v;j--;)
        q=j-(j>i),              /* source index in the old tree */
        y[j]=j-i?x[q]+(x[q]>=i):i?i+1:v,   /* ends shift by 1 at or after i */
        y[j+v]=j-i?x[*x+q]:c%3;             /* colours copied, new node gets c%3 */
}

/* f(d,k): depth-first search. Try every tree of size <= d+1 (index >= k) as the
   d-th element; keep it if no earlier element embeds into it. */
f(d,k){
  for(g(d+2),M+=d>M;*P[k]<d+2;~q?:f(d+1,1),k++)   /* ~q==0 means all checks passed */
    for(S[d]=y=P[k],q=d;q--&&(x=S[q])-y&&!F(0,*x,0,*y););
}

main(){
  *(P=realloc(0,8))=&M;   /* empty seed tree: points at M, which is 0 at this time */
  g(1);                   /* the three single-node trees */
  f(0,1);
  printf("%d",M);
}
