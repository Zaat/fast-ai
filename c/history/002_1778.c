/* TREE(n): trees stored in preorder; L=label, Z=subtree size */
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#define M 64
typedef struct{int n;char L[M],Z[M];}T;
static T*P;static int np,cap,lv,*lvl;static int N;
static int e(T*x,int i,T*y,int j);
static int mt(T*x,int i,int ie,T*y,int j,int je,unsigned u){ /* match children of x[i..ie) into distinct children of y[j..je) */
  if(i>=ie)return 1; int k=0;
  for(int c=j;c<je;c+=y->Z[c],k++) if(!(u>>k&1)&&e(x,i,y,c)&&mt(x,i+x->Z[i],ie,y,j,je,u|1u<<k))return 1;
  return 0;}
static int e(T*x,int i,T*y,int j){
  for(int c=j+1;c<j+y->Z[j];c+=y->Z[c]) if(e(x,i,y,c))return 1;
  return x->L[i]==y->L[j]&&mt(x,i+1,i+x->Z[i],y,j+1,j+y->Z[j],0);}
static void add(T*t){ for(int k=0;k<np;k++) if(P[k].n==t->n&&!memcmp(P[k].L,t->L,t->n)&&!memcmp(P[k].Z,t->Z,t->n))return;
  if(np==cap)P=realloc(P,(cap=cap?cap*2:64)*sizeof(T)); P[np++]=*t;}
static void grow(void){ /* make all trees with lv+1 nodes from trees with lv nodes */
  int a=lvl[lv-1],b=lvl[lv];
  for(int k=a;k<b;k++) for(int i=0;i<P[k].n;i++) for(int c=0;c<N;c++){
    T t=P[k]; int p=i+t.Z[i];
    memmove(t.L+p+1,t.L+p,t.n-p); memmove(t.Z+p+1,t.Z+p,t.n-p);
    t.L[p]=c;t.Z[p]=1;t.n++;
    for(int j=0;j<=i;j++) if(j+P[k].Z[j]>i)t.Z[j]++;
    add(&t);}
  lvl=realloc(lvl,(lv+2)*sizeof(int)); lvl[++lv]=np;}
static T*S[1<<16];
static int f(int d){ /* longest continuation from sequence S[0..d) */
  while(lv<d+1)grow(); int best=d;
  for(int k=0;k<lvl[d+1];k++){ int ok=1;
    for(int p=0;p<d&&ok;p++) if(e(S[p],0,&P[k],0))ok=0;
    if(ok){S[d]=&P[k]; int r=f(d+1); if(r>best)best=r;}}
  return best;}
int main(int c,char**v){ N=c>1?atoi(v[1]):3;
  lvl=malloc(2*sizeof(int)); lvl[0]=0;
  for(int k=0;k<N;k++){T t={1};t.L[0]=k;t.Z[0]=1;add(&t);} lvl[1]=np; lv=1;
  printf("%d\n",f(0)); return 0;}
