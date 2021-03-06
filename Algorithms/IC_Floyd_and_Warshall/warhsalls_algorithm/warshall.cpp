#include <iostream>
#include <vector>

using namespace std;

ostream & operator<<( ostream & os, vector< vector< int > > & rhs )
{	for ( int i = 0; i<rhs.size(); i++ )
	{	for ( int j=0; j< rhs[i].size(); j++ )
				os << rhs[i][j] << " ";
				os << endl;
    }
	return os;
}


void Warshall(  vector< vector< int > > & R, vector< vector< int > > & A)
{
        vector< vector<int> > RKM1;  // R( k - 1 )
        RKM1 = R = A;

        int n = A.size();
        for ( int k=0; k < n; k++ )
        {
                RKM1 = R;  // Save R( k - 1 ) to make R( k )
          for (int i = 0; i < n; i++)
          {
            for (int j = 0; j < n; j++)
            {
              R[i][j] = RKM1[i][j]
            }
          }
				// Complete Warshall's aglorithm here

                cout << R << endl;
        }
}


int main()
{
        vector< vector<int> > A;
        vector< vector<int> > R;

        A.push_back( vector<int>() );
        A.back().push_back( 0 );
        A.back().push_back( 1 );
        A.back().push_back( 0 );
        A.back().push_back( 0 );

        A.push_back( vector<int>() );
        A.back().push_back( 0 );
        A.back().push_back( 0 );
        A.back().push_back( 0 );
        A.back().push_back( 1 );

        A.push_back( vector<int>() );
        A.back().push_back( 0 );
        A.back().push_back( 0 );
        A.back().push_back( 0 );
        A.back().push_back( 0 );

        A.push_back( vector<int>() );
        A.back().push_back( 1 );
        A.back().push_back( 0 );
        A.back().push_back( 1 );
        A.back().push_back( 0 );

        Warshall( R, A );

        return 0;
}