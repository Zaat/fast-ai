#include <stdio.h>
#include <stdlib.h>
typedef struct T{int l,n;struct T**c;}T;typedef struct{T**v;int n;}V;
int E(T*,T*);
void A(V*x,T*t){x->v=realloc(x->v,(x->n+1)*sizeof *x->v);x->v[x->n++]=t;}
T*N(int l,int n){T*t=malloc(sizeof *t);t->l=l;t->n=n;t->c=n?malloc(n*sizeof *t->c):0;return t;}
T*C(T*t){T*u=N(t->l,t->n);for(int i=0;i<t->n;i++)u->c[i]=C(t->c[i]);return u;}
int M(T*a,T*b,int i,char*u){if(i==a->n)return 1;for(int j=0;j<b->n;j++)if(!u[j]&&E(a->c[i],b->c[j])){u[j]=1;if(M(a,b,i+1,u))return 1;u[j]=0;}return 0;}
int E(T*a,T*b){for(int i=0;i<b->n;i++)if(E(a,b->c[i]))return 1;if(a->l!=b->l||a->n>b->n)return 0;char*u=calloc(b->n,1);int r=M(a,b,0,u);free(u);return r;}
void G(T*t,int n,V*out){for(int l=0;l<n;l++){T*u=N(t->l,t->n+1);for(int j=0;j<t->n;j++)u->c[j]=C(t->c[j]);u->c[t->n]=N(l,0);A(out,u);}for(int i=0;i<t->n;i++){V z={0};G(t->c[i],n,&z);for(int k=0;k<z.n;k++){T*u=N(t->l,t->n);for(int j=0;j<t->n;j++)u->c[j]=j==i?z.v[k]:C(t->c[j]);A(out,u);}free(z.v);}}
int S(int n,V*s,V q){int best=0;for(int i=0;i<s->n;i++){int ok=1;for(int j=0;j<q.n;j++)if(E(q.v[j],s->v[i])){ok=0;break;}if(ok){V z={malloc(s->n*sizeof *z.v),s->n},w={malloc((q.n+1)*sizeof *w.v),q.n+1};for(int j=0;j<s->n;j++)z.v[j]=s->v[j];for(int j=0;j<s->n;j++)G(s->v[j],n,&z);for(int j=0;j<q.n;j++)w.v[j]=q.v[j];w.v[q.n]=s->v[i];int x=1+S(n,&z,w);if(x>best)best=x;free(z.v);free(w.v);}}return best;}
int main(int c,char**v){int n=c>1?atoi(v[1]):3;V s={malloc(n*sizeof *s.v),n},q={0};for(int i=0;i<n;i++)s.v[i]=N(i,0);printf("%d\n",S(n,&s,q));}
