#include<bits/stdc++.h>
using namespace std;
#define rep(i,a,n) for(int i=a;i<=n;i++)
#define ll long long
#define pb push_back
 
const ll inf=1e18;
const int N=2e5+10;
#define pii pair<int ,int > 
 
 
 
int n,m,k;
 
struct node
{
    int id,c;
    node(int a,int b)
    {
        id=a;
        c=b;
    }    
};
 
 
vector<node> v[N];
vector<pii > p[N];
int x[N],l[N],r[N];
 
bool flagb=1;
 
int sum[N];
 
int col[N];
 
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
  
    cin>>n>>m>>k;
  
    
    rep(i,1,n)
    {
        int cc;
        cin>>cc;
        col[i]=cc;
        if(cc>i)
        {
            flagb=0;
        }
        
        sum[i]=sum[i-1];
        if( col[i-1]!=col[i])
        {
            sum[i]++;
        }
        
        v[1].pb(  node(i,cc)   );
    }
    rep(i,1,k)
    {
        cin>>x[i]>>l[i]>>r[i];
    }

    if(flagb)
    {
        
        p[1].pb({1,n});
        
    
        
        rep(i,1,k)
        {    
        int ans=0;
            vector<pii > temp;
            for(auto j:p[x[i]])
            {
                int leftt=j.first,rightt=j.second;
                if(rightt<l[i]||r[i]<leftt)
                {
                    temp.pb(j);
                }
                else 
                {
                    if(l[i]<=leftt)
                    {
                        if(r[i]<rightt)
                        {
                            p[i+1].pb(  {leftt,r[i]}   );
                            temp.pb({r[i]+1,rightt});
                        }
                        else
                        {
                            p[i+1].pb({leftt,rightt});
                        }
                    }
                    else 
                    {
                        if(r[i]<rightt)
                        {
                            p[i+1].pb(  {   l[i]   ,r[i] }      );
                            temp.pb( {leftt,l[i]-1}    );
                            temp.pb({r[i]+1,rightt});
                        }
                        else
                        {
                            p[i+1].pb(  {   l[i]   ,rightt }      );
                            temp.pb( { leftt , l[i]-1 }       );
                        }
                    }
                }
            }
            p[x[i]]=temp;
            
            int duan=0;
            int lasttc=0;
            
            
            for(auto j:p[i+1])
            {              
                duan+=col[j.second]-col[j.first]+1;
                if(lasttc==col[j.first])
                {
                    duan--;
                }
                
                lasttc=col[j.second];
                
            }
            cout<<duan<<" "<<duan<<endl; 
            
        }
        
        
        exit(0);
    }
    
    
    
        rep(i,1,k)
    {
        vector<node > temp;
        for(auto j:v[  x[i]  ]    )
        {
            if(l[i]<=j.id&&j.id<=r[i])
            {
                v[i+1].pb(j);
            }
            else
            {
                temp.pb(j);
            }
        }
        v[x[i]]=temp;
        set<int > yanse;
        int duan=0;
        int lastt=0;
        for(auto j:v[i+1])
        {
            if(j.c!=lastt)
            {
                duan++;
                lastt=j.c;
            }
            yanse.insert(j.c);
        }
        cout<<yanse.size()<<" "<<duan<<endl;
    }
        exit(0);
    
    
    
    return 0;
}

