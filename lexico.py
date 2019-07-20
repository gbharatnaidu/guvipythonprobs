#include <stdio.h>
#include <stdlib.h>
int main()
{
int i,j,n;
scanf("%d",&n);
char a[n][10];
char temp[10];
for(i=0;i<n;i++){
    scanf("%s",a[i]);
}
for(i=0;i<n;i++){
        for(j=0;j<n-1;j++)
    if(strcmp(a[j],a[j+1])>0){
        strcpy(temp,a[j]);
        strcpy(a[j],a[j+1]);
        strcpy(a[j+1],temp);
    }
}
printf("%s",a[0]);

    return 0;
}
