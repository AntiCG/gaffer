##########################################################################
#  
#  Copyright (c) 2011, John Haddon. All rights reserved.
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

import GafferUI

class TabbedContainer( GafferUI.ContainerWidget ) :

	def __init__( self ) :
	
		GafferUI.ContainerWidget.__init__( self, QtGui.QTabWidget() )
		
		self._qtWidget().setUsesScrollButtons( False )
		
		self.__widgets = []
								
	def append( self, child, label="" ) :
	
		oldParent = child.parent()
		if oldParent :
			oldParent.removeChild( child )
		
		self.__widgets.append( child )
		self._qtWidget().addTab( child._qtWidget(), label )
				
	def remove( self,  child ) :
	
		self.removeChild( child )
		
	def setLabel( self, child, labelText ) :
	
		self._qtWidget().setTabText( self.__widgets.index( child ), labelText )
			
	def getLabel( self, child ) :
		
		return str( self._qtWidget().tabText( self.__widgets.index( child ) ) )
	
	def setCurrent( self, child ) :
	
		self._qtWidget().setCurrentIndex( self.__widgets.index( child ) )

	def getCurrent( self ) :
	
		if not self.__widgets :
			return None
			
		return self.__widgets[ self._qtWidget().currentIndex() ]
		
	def __getitem__( self, index ) :
	
		return self.__widgets[index]
	
	def __delitem__( self, index ) :
	
		self.removeChild( self.__widgets[index] )
	
	def __len__( self ) :
	
		return len( self.__widgets )
		
	def removeChild( self, child ) :
	
		self._qtWidget().removeTab( self.__widgets.index( child ) )
		self.__widgets.remove( child )
