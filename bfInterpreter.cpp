#include <iostream>
#include <fstream>

using namespace std;

int main(){
    string filePath;
    
    cout << "File path: ";
    getline(cin, filePath);
    system("cls");

    string code;
    getline(ifstream(filePath), code, '\0');

    int memory[999]; for (int i=0; i<999; i++) { memory[i]=0; }
    int ptr=0;

    for (int i=0; i<code.size(); i++){
        char codeChar = code[i];

        if (codeChar==char('<')) { ptr-=1; }
        if (codeChar==char('>')) { ptr+=1; }
        if (codeChar==char('+')) { memory[ptr]+=1; }
        if (codeChar==char('-')) { memory[ptr]-=1; if (ptr<0) { cout << "Error in code"; cin.ignore(); return 0; } }
        if (codeChar==char('.')) { cout << char(memory[ptr]); }
        if (codeChar==char(',')) { char c = getchar(); memory[ptr] = int(c); }

        if (codeChar==char('[')){
            if (memory[ptr]==0){
                int indent = 0;
                while (i <= code.size()){

                    i++;
                    if (i >= code.size()){
                        cout << "Error in code";
                        cin.ignore();
                        return 0;
                    }
                    if (code[i]==char('[')) indent++;
                    if (code[i]==char(']')){
                        if (indent>0) indent--;
                        else{
                            break;
                        }
                    }

                }
            }
        }

        if (codeChar==char(']')){
            if (memory[ptr]!=0){
                int indent = 0;
                while (i >= -1){

                    i--;
                    if (i < 0){
                        cout << "Error in code";
                        cin.ignore();
                        return 0;
                    }
                    if (code[i]==char(']')) indent++;
                    if (code[i]==char('[')){
                        if (indent>0) indent--;
                        else{
                            break;
                        }
                    }

                }
            }
        }

    }

    cout << endl << "Code finished";
    cin.ignore();

    return 0;
}