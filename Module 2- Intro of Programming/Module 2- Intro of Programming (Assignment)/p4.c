#include<stdio.h>
main(){
	int a,b,c;
	float d;
	printf("\n enter first number :");
	scanf("%d",&a);
	
	printf("\n enter second number :");
	scanf("%d",&b);
	c=a+b;
	printf("\n Addition of %d and %d is %d",a,b,c);
	c=a-b;
	printf("\n Subtraction of %d and %d is %d",a,b,c);
	c=a*b;
	printf("\n Multiplication of %d and %d is %d",a,b,c);
	d=a/b;
	printf("\n Division of %d and %d is %f",a,b,d);
	
	printf("\n enter your age :");
	scanf("%d",&a);
	
	if(a>=18){
		printf("\n you are eligible for voting");
	}
	else{
		printf("\n you are not eligible for voting");
	}
}
