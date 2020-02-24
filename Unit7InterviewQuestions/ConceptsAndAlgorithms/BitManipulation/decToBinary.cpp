#include<iostream>
using namespace std;
void decToBinary(int num){
    for( int i=31;i>=0;i--){
        int k = num>>i;
        if(k & 1){
            cout<<"1";
        }
        else{
            cout<<"0";
        }
    }
    return;
}
int main(){
    int num;
    cin>>num;
    cout<<"Convert decimel to binary\n";
    decToBinary(num);
    return 0;
}