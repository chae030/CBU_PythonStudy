#include <stdio.h>

int main() {
    int n, m, i, j;
    scanf("%d %d", &n, &m);
    
    char s[n][m+1];
    for(i=0;i<n;i++){
        scanf("%s", s[i]);
    }
    
    long long res[26] = {0};
    for(i=0;i<n;i++){
        for(j=0;j<m;j++){
            long long temp = 0;
            
            temp += (long long)(i+1)*(j+1)*(2*n-i)*(2*m-j);
            temp += (long long)(n+i+1)*(j+1)*(n-i)*(2*m-j);
            temp += (long long)(i+1)*(m+j+1)*(2*n-i)*(m-j);
            temp += (long long)(n+i+1)*(m+j+1)*(n-i)*(m-j);
            
            res[s[i][j]-'A'] += temp;
        }
    }
    
    for(i=0;i<26;i++) printf("%lld\n", res[i]);
    
    return 0;
}