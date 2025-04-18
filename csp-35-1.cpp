#include<iostream>
	using namespace std;
	int result(string a){
		int length=a.length();
		int flag1=0;
		int flag2=0;
		int flag3=0;
		for(int i=0;i<length;i++){
			if((a[i]<='z'&&a[i]>='a')||(a[i]>='A'&&a[i]<='Z')){
				flag1=1;
				continue;
			}
			if(a[i]>='0'&&a[i]<='9'){
				flag2=1;
				continue;
			}
			if(a[i]=='*'||a[i]=='#'){
				flag3=1;
				continue;
			}
		}
		int count=1;
		int flag=0;
		if(flag1&&flag2&&flag3){
			for(int i=0;i<length;i++){
				count=1;
				for(int j=i+1;j<length;j++){
					if(a[i]==a[j])	count++;	
				}
				if(count>2)	return 1;
			}
			return 2;
		}
		else	return 0;
	}
	int main(){
		int n;
		cin>>n;
		int b[101];
		for(int i=1;i<=n;i++){
			string a;
			cin>>a;
			b[i]=result(a);
		}
		for(int i=1;i<=n;i++){
			cout<<b[i]<<endl;
		}
	}
