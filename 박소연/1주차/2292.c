#include <stdio.h>

int hmm(int n){
    int temp;
    
    if(n == 1){
        return 1;
    }
    else{
        temp = hmm(n-1) + (n-1)*6;
        return temp;
    }
}


int main() {
    int n, i = 1;
    
    scanf("%d", &n);
    
    while(1){
        if((n / hmm(i)) >= 1 && n != hmm(i)){
            i++;
        }
        else{
            break;
        }
    }
    
    printf("%d", i);
    
    return 0;
}