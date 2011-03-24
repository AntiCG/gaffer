//////////////////////////////////////////////////////////////////////////
//  
//  Copyright (c) 2011, John Haddon. All rights reserved.
//  
//  Redistribution and use in source and binary forms, with or without
//  modification, are permitted provided that the following conditions are
//  met:
//  
//      * Redistributions of source code must retain the above
//        copyright notice, this list of conditions and the following
//        disclaimer.
//  
//      * Redistributions in binary form must reproduce the above
//        copyright notice, this list of conditions and the following
//        disclaimer in the documentation and/or other materials provided with
//        the distribution.
//  
//      * Neither the name of John Haddon nor the names of
//        any other contributors to this software may be used to endorse or
//        promote products derived from this software without specific prior
//        written permission.
//  
//  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
//  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
//  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
//  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
//  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
//  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
//  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
//  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
//  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
//  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
//  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
//  
//////////////////////////////////////////////////////////////////////////

#ifndef GAFFERUI_STANDARDNODEGADGET_H
#define GAFFERUI_STANDARDNODEGADGET_H

#include "GafferUI/NodeGadget.h"

namespace GafferUI
{

IE_CORE_FORWARDDECLARE( LinearContainer )

class StandardNodeGadget : public NodeGadget
{

	public :
	
		IE_CORE_DECLARERUNTIMETYPEDEXTENSION( StandardNodeGadget, StandardNodeGadgetTypeId, NodeGadget );

		StandardNodeGadget( Gaffer::NodePtr node );
		virtual ~StandardNodeGadget();

		virtual NodulePtr nodule( Gaffer::ConstPlugPtr plug );
		virtual ConstNodulePtr nodule( Gaffer::ConstPlugPtr plug ) const;
		
		Imath::Box3f bound() const;

	protected :
	
		virtual void doRender( IECore::RendererPtr renderer ) const;

	private :
	
		NodulePtr addNodule( Gaffer::PlugPtr plug );
	
		static NodeGadgetTypeDescription<StandardNodeGadget> g_nodeGadgetTypeDescription;
		
		bool m_nodeHasObjectPlugs;
		
		typedef std::map<const Gaffer::Plug *, Nodule *> NoduleMap;
		NoduleMap m_nodules;
				
		void selectionChanged( Gaffer::SetPtr selection, IECore::RunTimeTypedPtr node );
		void childAdded( Gaffer::GraphComponentPtr parent, Gaffer::GraphComponentPtr child );
		void childRemoved( Gaffer::GraphComponentPtr parent, Gaffer::GraphComponentPtr child );

};

} // namespace GafferUI

#endif // GAFFERUI_STANDARDNODEGADGET_H