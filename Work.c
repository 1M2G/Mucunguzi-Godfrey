#include<stdio.h>
int main(){
int tution,prov,full,pay;
tution=2500000;
prov=((0.1)*tution);
full=tution;
pay=300000;
printf("Tution bar %d\n",tution);
printf("Prov reg bar %d\n",prov);
printf("Full reg bar %d\n",full);
if(pay>=full)
{
printf("FULL REGISTRATION\n");
}
else
{
printf("DONT QUALIFY FOR FULL REGISTRATION\n");
}

return 0;

}
