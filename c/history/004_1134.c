#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define L(t,i)t[1+(i)]
#define Z(t,i)t[1+*t+(i)]
int**P,**S,p,N,*l,v,e();
m(int*x,int i,int I,int*y,int j,int J,char*u){if(i>=I)return 1;for(int c=j;c<J;c+=Z(y,c))if(!u[c]&&e(x,i,y,c)){u[c]=1;if(m(x,i+Z(x,i),I,y,j,J,u))return 1;u[c]=0;}return 0;}
e(int*x,int i,int*y,int j){for(int c=j+1;c<j+Z(y,j);c+=Z(y,c))if(e(x,i,y,c))return 1;if(L(x,i)-L(y,j))return 0;char u[*y];memset(u,0,*y);return m(x,i+1,i+Z(x,i),y,j+1,j+Z(y,j),u);}
g(){int k=l[v-1],h=l[v],i,c,j,n,q,r,*o,*t;for(;k<h;k++)for(o=P[k],n=*o,i=0;i<n;i++)for(c=0;c<N;c++){q=i+Z(o,i);t=malloc(sizeof*t*(2*n+3));*t=n+1;for(j=0;j<=n;j++)r=j-(j>q),L(t,j)=j-q?L(o,r):c,Z(t,j)=j-q?Z(o,r)+(r<=i&&r+Z(o,r)>i):1;P=realloc(P,sizeof*P*(p+1));P[p++]=t;}l=realloc(l,sizeof*l*(v+2));l[++v]=p;}
f(d){int b=d,k=0,q,r;while(v<=d)g();S=realloc(S,sizeof*S*(d+1));for(;k<l[d+1];k++){for(q=0;q<d&&!e(S[q],0,P[k],0);q++);if(q==d){S[d]=P[k];r=f(d+1);b=r>b?r:b;}}return b;}
main(c,a)char**a;{N=c>1?atoi(a[1]):3;l=calloc(2,sizeof*l);for(;p<N;p++)P=realloc(P,sizeof*P*(p+1)),P[p]=malloc(3*sizeof**P),P[p][0]=P[p][2]=1,P[p][1]=p;l[v=1]=p;printf("%d\n",f(0));}
