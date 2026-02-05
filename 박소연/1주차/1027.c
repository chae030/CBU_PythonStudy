#include <stdio.h>

int main() {
    int n, i, j;
    scanf("%d", &n);
    long long height[n];
    for(i=0;i<n;i++) scanf("%lld", &height[i]);
    
    int res = 0;
    for(i=0;i<n;i++){
        int count = 0;
        
        long long maxn = 0, maxd = 1;
        for(j=i+1;j<n;j++){
            long long num = height[j] - height[i];
            long long d = j - i;
            if(j==i+1 || num*maxd > maxn*d){
                count++;
                maxn = num;
                maxd = d;
            }
        }
        
        long long minn = 0, mind = 1;
        for(j=i-1;j>=0;j--){
            long long num = height[j] - height[i];
            long long d = j - i;
            if(j==i-1 || num*mind < minn*d){
                count++;
                minn = num;
                mind = d;
            }
        }
        
        if (count > res) res = count;
    }
    
    printf("%d", res);
    
    return 0;
}