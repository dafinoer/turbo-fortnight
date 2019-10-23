

/*
Hackerrank -> Practise -> Algorithms -> Implementation 
Difficulty level - Hard
Test Cases Solved - All
Code by Paritosh Mahajan , Github profile - https://github.com/paritoshM9 , hackerrank profile - https://www.hackerrank.com/paritosh_mahajan
https://www.hackerrank.com/challenges/matrix-rotation-algo/problem
*/

#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

// Complete the matrixRotation function below.
void matrixRotation(vector<vector<int>> matrix, int r) {
    vector<vector<int>> matrix_copy = matrix;
    
    
    int num_row = matrix.size();
    int num_col = matrix[0].size();
    int r_real; //no of rotations
    int min = 0;
    int n ;
    if(num_row>num_col){
        min = num_col;
    }
    else{
        min = num_row;
    }
    int loop;
    int j;
    int row_min,row_max,col_min,col_max;
    

    j = 1;
    loop = min/2;
    row_min = 0;
    row_max = num_row - 1;
    col_min = 0;
    col_max = num_col - 1;
    while(j<=loop){
        n = 1;
        r_real = r % (2*num_row + 2*num_col - 4 - 8*(j-1));
        while(n <= r_real){
            for(int i=row_min;i<row_max;i++)
            {
                matrix_copy[i+1][col_min] = matrix[i][col_min];
            }
            for(int i=col_min;i<col_max;i++)
            {
                matrix_copy[row_max][i+1] = matrix[row_max][i];
            }
            for(int i=row_min+1;i<row_max+1;i++)
            { 
                matrix_copy[i-1][col_max] = matrix[i][col_max];
            }
            for(int i=col_min+1;i<col_max+1;i++)
            {
                matrix_copy[row_min][i-1] = matrix[row_min][i];
            }

            n++;
            matrix = matrix_copy;
        }
            row_min += 1;
            row_max -=1 ;
            col_min +=1;
            col_max -= 1;
            j++;

    }

    for(int j=0;j<num_row;j++){
        for (int k=0;k<num_col;k++)
        {
            cout<<matrix_copy[j][k]<<" ";
        }
        cout<<"\n";
    }
    
    

}

int main()
{
    string mnr_temp;
    getline(cin, mnr_temp);

    vector<string> mnr = split_string(mnr_temp);

    int m = stoi(mnr[0]);

    int n = stoi(mnr[1]);

    int r = stoi(mnr[2]);

    vector<vector<int>> matrix(m);
    for (int i = 0; i < m; i++) {
        matrix[i].resize(n);

        for (int j = 0; j < n; j++) {
            cin >> matrix[i][j];
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    matrixRotation(matrix, r);

    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}
