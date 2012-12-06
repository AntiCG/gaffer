##########################################################################
#  
#  Copyright (c) 2012, John Haddon. All rights reserved.
#  Copyright (c) 2012, Image Engine Design Inc. All rights reserved.
#  
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#  
#      * Redistributions of source code must retain the above
#        copyright notice, this list of conditions and the following
#        disclaimer.
#  
#      * Redistributions in binary form must reproduce the above
#        copyright notice, this list of conditions and the following
#        disclaimer in the documentation and/or other materials provided with
#        the distribution.
#  
#      * Neither the name of John Haddon nor the names of
#        any other contributors to this software may be used to endorse or
#        promote products derived from this software without specific prior
#        written permission.
#  
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
#  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
#  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
#  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
#  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#  
##########################################################################

import os
import unittest

import IECore

import Gaffer
import GafferTest
import GafferScene
import GafferSceneTest

class SubTreeTest( GafferSceneTest.SceneTestCase ) :
		
	def testPassThrough( self ) :
	
		a = GafferScene.AlembicSource()
		a["fileName"].setValue( os.path.dirname( __file__ ) + "/alembicFiles/animatedCube.abc" )	
		
		s = GafferScene.SubTree()
		s["in"].setInput( a["out"] )
		
		self.assertSceneValid( s["out"] )

		self.assertScenesEqual( a["out"], s["out"] )
		## \todo We should be able to remove the pathsToIgnore
		self.assertSceneHashesEqual( a["out"], s["out"], pathsToIgnore = [ "/" ] )	
		
	def testSubTree( self ) :
	
		a = GafferScene.AlembicSource()
		a["fileName"].setValue( os.path.dirname( __file__ ) + "/alembicFiles/animatedCube.abc" )	
		
		s = GafferScene.SubTree()
		s["in"].setInput( a["out"] )
		s["root"].setValue( "pCube1" )
		
		self.assertSceneValid( s["out"] )
		self.assertScenesEqual( s["out"], a["out"], scenePlug2PathPrefix = "/pCube1" )

	@GafferTest.expectedFailure
	def testRootHashesEqual( self ) :
	
		# this can be fixed by introducing hash*() methods in SceneNode, and making sure
		# they're not called for / when compute*() won't be called.
	
		a = GafferScene.AlembicSource()
		a["fileName"].setValue( os.path.dirname( __file__ ) + "/alembicFiles/animatedCube.abc" )	
		
		s = GafferScene.SubTree()
		s["in"].setInput( a["out"] )
		
		self.assertSceneValid( s["out"] )
		self.assertPathHashesEqual( a["out"], "/", s["out"], "/" )
		
if __name__ == "__main__":
	unittest.main()