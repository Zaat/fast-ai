typedef struct{char L[64],Z[64];}T;T P[1<<20],*S[99];p,N,l[99],v;
e(x,i,y,j)T*x,*y;{for(int c=j+1;c<j+y->Z[j];c+=y->Z[c])if(e(x,i,y,c))return 1;return x->L[i]==y->L[j]&&m(x,i+1,i+x->Z[i],y,j+1,j+y->Z[j],0);}
m(x,i,I,y,j,J,u)T*x,*y;{for(int c=j,k=0;i<I&&c<J;c+=y->Z[c],k++)if(!(u>>k&1)&&e(x,i,y,c)&&m(x,i+x->Z[i],I,y,j,J,u|1<<k))return 1;return i>=I;}
g(){int k=l[v-1],i,c,j,q;for(;k<l[v];k++)for(i=0;i<P[k].Z[0];i++)for(c=0;c<N;c++){T t=P[k];q=i+t.Z[i];memmove(t.L+q+1,t.L+q,63-q);memmove(t.Z+q+1,t.Z+q,63-q);t.L[q]=c;t.Z[q]=1;for(j=0;j<=i;j++)t.Z[j]+=j+P[k].Z[j]>i;P[p++]=t;}l[++v]=p;}
f(d){int b=d,k=0,q,r;while(v<=d)g();for(;k<l[d+1];k++){for(q=0;q<d&&!e(S[q],0,P+k,0);q++);if(q==d){S[d]=P+k;r=f(d+1);b=r>b?r:b;}}return b;}
main(c,a)char**a;{N=c>1?atoi(a[1]):3;for(;p<N;p++)P[p].L[0]=p,P[p].Z[0]=1;l[v=1]=p;printf("%d",f(0));}
