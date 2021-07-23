
from random import choice


def simulateWalk( distance:int ) -> int:
    ''' Returns "some" distance travelled from staring position '''
    movableDirections = { 'N':[ 0, 1 ], 'S':[ 0, -1 ], 'E':[ 1, 0 ], 'W':[ -1, 0 ] }
    currentPosition = [ 0, 0 ]

    sumLists = lambda x,y: x+y
    for _ in range( distance ):
        currentPosition = list( map( sumLists, currentPosition, movableDirections[ choice( 'NSEW' ) ] ) )

    return abs( currentPosition[ 0 ] ) +abs( currentPosition[ 1 ] )



def findLongestWalk( withinRange:int, maxWalkLength:int, cyclesPerWalk:int ) -> tuple( ( int, float ) ):
	longestWalk, longestWalkPCT = None, None

	for DST in range( withinRange, maxWalkLength ):
	    walksWithinRange = 0
	    
	    for _ in range( cyclesPerWalk ):
	        if simulateWalk( DST ) <= withinRange: walksWithinRange +=1

	    withinRangePCT = float( walksWithinRange ) / cyclesPerWalk
	    if withinRangePCT >= 0.5: longestWalk, longestWalkPCT = DST, withinRangePCT

	    print( f'Walk length ({DST :0>2d}) -> ({withinRangePCT :.2%})' )
	
	return longestWalk, longestWalkPCT



if __name__ == '__main__':
	nSteps = 4
	L_Walk, PCT = findLongestWalk( withinRange=nSteps, maxWalkLength=31, cyclesPerWalk=1000 )

	print( '\nLongest walk where you will be (on average) less' )
	print( 'then {} steps from the starting position -> {} @{:.2%}'.format( nSteps, L_Walk, PCT ) )
