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

import GafferUI

class PathChooserWidget( GafferUI.Widget ) :

	def __init__( self, path ) :
	
		GafferUI.Widget.__init__( self, QtGui.QWidget() )
		
		## \todo How many places are we doing this? Perhaps we could pass
		# a GafferUI.Widget to the constructor instead and have this done for us?
		self._qtWidget().setLayout( QtGui.QGridLayout() )
		self._qtWidget().layout().setSpacing( 0 )
		self._qtWidget().layout().setContentsMargins( 0, 0, 0, 0 )
		
		self.__path = path
		
		self.__column = GafferUI.ListContainer( GafferUI.ListContainer.Orientation.Vertical, spacing=8 )
		self._qtWidget().layout().addWidget( self.__column._qtWidget(), 0, 0 )
		
		self.__directoryListing = GafferUI.PathListingWidget( self.__path )
		self.__column.append( self.__directoryListing, True )
		
		self.__pathWidget = GafferUI.PathWidget( self.__path )
		self.__column.append( self.__pathWidget )
		
		self.__pathSelectedSignal = GafferUI.WidgetSignal()

		self.__listingSelectedConnection = self.__directoryListing.pathSelectedSignal().connect( self.__pathSelected )
		self.__pathWidgetSelectedConnection = self.__pathWidget.activatedSignal().connect( self.__pathSelected )

	## Returns the PathWidget used for text-based path entry.
	def pathWidget( self ) :
	
		return self.__pathWidget

	## This signal is emitted when the user has selected a path.
	def pathSelectedSignal( self ) :
	
		return self.__pathSelectedSignal

	# This slot is connected to the pathSelectedSignals of the children and just forwards
	# them to our own pathSelectedSignal.
	def __pathSelected( self, childWidget ) :
		
		self.pathSelectedSignal()( self )