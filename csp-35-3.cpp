#include<bits/stdc++.h>
using namespace std;
#define rep(i,a,n) for(int i=a;i<=n;i++)
#define ll long long
#define pb push_back
 
const ll inf=1e18;
const int N=2e5+10;
#define pii pair<int ,int > 
 
 
 
string ss[N],s,t;
 
int a[10];
 
vector<string > v;
 
vector<string > yuan,zong;
 
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);

 
    int n;
    cin>>n;
    getline(cin,t);
    rep(i,1,n)
    {
        getline(cin,ss[i]);
    }
 
 
    int flag=0;
    while(getline(cin,s))
    {
 
        if(flag==1)
        {
 
            
            if(s[0]!='+')
            {
                string temp="";
                
                
                int len=s.size();
                rep(i,1,len-1)
                {
                    temp=temp+s[i];
                
                }
 
                yuan.pb(temp);
            }
            if(s[0]!='-')
            {
                string temp="";
                
                int len=s.size();
                rep(i,1,len-1)
                {
                    temp=temp+s[i];
                
                }
                v.pb(temp);
            }
        }
        
        if(s[0]=='@'&&s[1]=='@')
        {
            flag=1;
            int lens=s.size();
            s=' '+s;
            int num=0,cnt=0;
            rep(i,1,lens)
            {
                if('0'<=s[i]&&s[i]<='9')
                {
                    num*=10;
                    num+=s[i]-'0';
                }
                else
                {
                    if(num)
                    {
                        a[++cnt]=num;
 
                        num=0;
                    }
                }
            }
 
        }
    }
 
    
    int siz=yuan.size();
 
    rep(i,1,n)
    {
        bool flag=1;
        int cnt=0;
        rep(j,i,i+siz-1)
        {
            
            if(yuan[cnt  ]!=ss[j])
            {
                flag=0;
                break;
            }
            cnt++;
        }
        if(flag)
        {
            a[1]=i;
            break;
        }
    }
    
    bool fla=0;
    rep(i,1,n)
    {
        if(i<a[1]  || a[1]+a[2]-1<i)
        {
            cout<<ss[i]<<endl;
        }
        else if(fla==0)
        {
            fla=1;
            for(auto j:v)
            {
                cout<<j<<endl;
            }
        }
     }
    
    return 0;
}

