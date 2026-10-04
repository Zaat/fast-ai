void*realloc();int**P,**S,p,N,v=1,e();
m(x,i,I,y,j,J,u)int*x,*y;char*u;{for(int c=j;i<I&&c<J;c+=y[c])if(!u[c]&&e(x,i,y,c)&&(u[c]=m(x,i+x[i],I,y,j,J,(u[c]=1,u))))return 1;return i>=I;}
e(x,i,y,j)int*x,*y;{for(int c=j+1;c<j+y[j];c+=y[c])if(e(x,i,y,c))return 1;char u[*y];memset(u,0,*y);return x[*x+i]==y[*y+j]&&m(x,i+1,i+x[i],y,j+1,j+y[j],u);}
g(){int h=p,k=0,i,c,j,q,r,*o,*t;for(;k<h;k++)if(*(o=P[k])==v)for(i=0;i<v;i++)for(c=N;c--;){q=i+o[i];t=realloc(0,8*v+8);for(j=0;j<=v;j++)r=j-(j>q),t[j]=j-q?o[r]+(r<=i&r+o[r]>i):1,t[v+1+j]=j-q?o[v+r]:c;P=realloc(P,8*p+8);P[p++]=t;}v++;}
f(d){int b=d,k=0,q,r;while(v<=d)g();S=realloc(S,8*d+8);for(;k<p&&*P[k]<d+2;k++){for(q=d;q--&&!e(S[q],0,P[k],0););if(q<0)S[d]=P[k],r=f(d+1),b=r>b?r:b;}return b;}
main(c,a)char**a;{for(N=c>1?atoi(*++a):3;p<N;)P=realloc(P,8*p+8),(P[p]=realloc(0,8))[1]=p,*P[p++]=1;printf("%d",f(0));}
