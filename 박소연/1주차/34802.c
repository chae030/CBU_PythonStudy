#include <stdio.h>

int main() {
    char s1[9];
    char s2[9];
    scanf("%s", s1);
    scanf("%s", s2);
    int t1 = (s1[0]-'0')*36000 + (s1[1]-'0')*3600 + (s1[3]-'0')*600 + (s1[4]-'0')*60 + (s1[6]-'0')*10 + (s1[7]-'0');
    int t2 = (s2[0]-'0')*36000 + (s2[1]-'0')*3600 + (s2[3]-'0')*600 + (s2[4]-'0')*60 + (s2[6]-'0')*10 + (s2[7]-'0');
    double t = t2 - t1;
    
    double n, k;
    scanf("%lf %lf", &n, &k);
    double tt = n - n*k/100;
    
    if(tt <= t) printf("1");
    else printf("0");
    
    return 0;
}