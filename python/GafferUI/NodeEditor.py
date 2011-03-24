##########################################################################
#  
#  Copyright (c) 2011, John Haddon. All rights reserved.
#  Copyright (c) 2011, Image Engine Design Inc. All rights reserved.
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

from PySide import QtGui

import IECore

import Gaffer
import GafferUI

class NodeEditor( GafferUI.NodeSetEditor ) :

	def __init__( self, scriptNode=None ) :
	
		GafferUI.NodeSetEditor.__init__( self, QtGui.QWidget(), scriptNode )
				
		self._qtWidget().setLayout( QtGui.QGridLayout() )
		self.__column = GafferUI.ListContainer( GafferUI.ListContainer.Orientation.Vertical )
		self._qtWidget().layout().addWidget( self.__column._qtWidget(), 0, 0 )
		
		self._updateFromSet()
				
	def __repr__( self ) :

		return "GafferUI.NodeEditor()"

	def _updateFromSet( self ) :
			
		if not hasattr( self, "_NodeEditor__column" ) :
			# we're being called during construction
			return
		
		del self.__column[:]
		
		node = self.getNodeSet().lastAdded()
		if not node :
			return
		
		self.__column.append( GafferUI.NameWidget( node ) )

		nodeHierarchy = IECore.RunTimeTyped.baseTypeIds( node.typeId() )
		for typeId in [ node.typeId() ] + nodeHierarchy :	
			uiBuilder = self.__uiBuilders.get( typeId, None )
			if uiBuilder is not None :
				break
						
		frame = GafferUI.Frame()
		self.__column.append( frame, expand=True )
		frame.setChild( uiBuilder( node ) )
	
	## \todo I think the factory belongs in NodeUI.
	__uiBuilders = {}
	@classmethod
	def registerNodeUI( cls, nodeType, uiBuilder ) :
	
		cls.__uiBuilders[nodeType] = uiBuilder	
				
GafferUI.EditorWidget.registerType( "NodeEditor", NodeEditor )