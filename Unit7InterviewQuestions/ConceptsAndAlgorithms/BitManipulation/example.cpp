#include<iostream>
using namespace std;
int repeatedArithmeticShift(int num, int shifts){
    cout<<"Shifting "<<num<<" by"<<shifts<<endl;
    for(int i=0;i<shifts;i++){
        num>>=1;
    }
    return num;
}

int repeatedLogicalShift(int num, int shifts){
    cout<<"Shifting "<<num<<" by"<<shifts<<endl;
    for(int i=0;i<shifts;i++){
        num >>= 1;
    }
    return num;
}

int main(){
    cout<<"Hello World\n";
    cout<<"\n"<<repeatedArithmeticShift(-93242,40)<<endl;
}
