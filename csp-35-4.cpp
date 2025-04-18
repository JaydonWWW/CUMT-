#include<bits/stdc++.h>
using namespace std;
#define rep(i,a,n) for(int i=a;i<=n;i++)
#define ll long long
#define pb push_back
 
const ll inf=1e18;
const int N=5e3+10;
 
 
 
 
int n,m;
 
ll x[N],y[N];
 
struct node
{
    int id;
    ll n_dis;
    node(int b,ll c)
    {
        id=b;
        n_dis=c;
    }
    bool operator < (const node &a) const
    {
        return n_dis>a.n_dis;
    }
};
 
struct edge
{
    int to;
    ll w;
    edge(int a,ll c)
    {
        to=a;
        w=c;
    }
};
 
 
 
vector<edge > e[N];
bool done[N];
ll dis[N];
 
 
 
 
void di()
{
    int s=1;
    rep(i,1,n)
    {
        dis[i]=inf;
        done[i]=0;
    }
    dis[s]=0;
    priority_queue<node > q;
    q.push(node(1,0));
    while(q.size())
    {
        node u=q.top();
        q.pop();
        if(done[u.id])
        {
            continue;
        }
        done[u.id]=1;
        for(int i=0;i<e[u.id].size();i++)
        {
            edge y=e[u.id][i];
            if(done[y.to])
            {
                continue;
            }
            if(dis[y.to]>y.w+u.n_dis)
            {
                dis[y.to]=y.w+u.n_dis;
                q.push(node(y.to,dis[y.to]));
            }
        }
    }
}
 
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);

    cin>>n>>m;
    rep(i,1,n)
    {
        cin>>x[i]>>y[i];
    }
    
    rep(i,1,m)
    {
        ll xx,yy,r,t;
        cin>>xx>>yy>>r>>t;
        vector<int > aa,bb;
        rep(j,1,n)
        {
            if(    xx-r<=x[j]&&x[j]<=xx+r&&yy-r<=y[j]&&y[j]<=yy+r)
            {
                aa.pb(j);
                bb.pb(j);
            }
        }
        for(auto ii:aa)
        {
            for(auto jj:bb)
            {
                if(ii==jj)
                {
                    continue;
                }
                e[ii].pb(edge(jj,t));
            }
        }
    }
    
    di();
    if(dis[n]==inf)
    {
        cout<<"Nan";exit(0);
    }
    cout<<dis[n];
    
    
    return 0;
}

