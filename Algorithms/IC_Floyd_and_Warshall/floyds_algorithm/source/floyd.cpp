#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAX_INT = 0x7FFFFFFF;

ostream & operator<<( ostream & os, vector< vector< int > > & rhs )
{	for ( int i = 0; i<rhs.size(); i++ )
	{	for ( int j=0; j< rhs[i].size(); j++ )
			os << rhs[i][j] << " ";
            os << endl;
    }
	return os;
}

void Floyd(  vector< vector< int > > & D, vector< vector< int > > & W )
{
        int n = W.size();
		D = W;
        for ( int k=0; k < n; k++ )
        {	

			// COMPLETE FLOYDS ALGORITHM HERE
            for(int i = 0; i < n; i++)
            {
                for(int j = 0; j < n; j++)
                {
                    D[i][j] = min(W[i][j], W[i][k] + W[k][j]);
                }
            }


			cout << D << endl;
        }
}


int main()
{
		cout << MAX_INT;
        vector< vector<int> > W;
        vector< vector<int> > D;

        W.push_back( vector<int>() );
        W.back().push_back( 0 );
        W.back().push_back( MAX_INT );
        W.back().push_back( 3 );
        W.back().push_back( MAX_INT );

        W.push_back( vector<int>() );
        W.back().push_back( 2 );
        W.back().push_back( 0 );
        W.back().push_back( MAX_INT );
        W.back().push_back( MAX_INT );

        W.push_back( vector<int>() );
        W.back().push_back( MAX_INT );
        W.back().push_back( 7 );
        W.back().push_back( 0 );
        W.back().push_back( 1 );

        W.push_back( vector<int>() );
        W.back().push_back( 6 );
        W.back().push_back( MAX_INT );
        W.back().push_back( MAX_INT );
        W.back().push_back( 0 );


        Floyd( D, W );

        return 0;
}