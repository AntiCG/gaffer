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

#ifndef GAFFER_COMPOUNDNUMERICPLUG_H
#define GAFFER_COMPOUNDNUMERICPLUG_H

#include "OpenEXR/ImathVec.h"
#include "OpenEXR/ImathColor.h"

#include "Gaffer/CompoundPlug.h"
#include "Gaffer/NumericPlug.h"

namespace Gaffer
{

template<typename T>
class CompoundNumericPlug : public CompoundPlug
{

	public :

		typedef T ValueType;
		typedef NumericPlug<typename T::BaseType> ChildType;
		
		IECORE_RUNTIMETYPED_DECLARETEMPLATE( CompoundNumericPlug<T>, CompoundPlug );

		CompoundNumericPlug(
			const std::string &name = staticTypeName(),
			Direction direction=In,
			T defaultValue = T( 0 ),
			T minValue = T( Imath::limits<typename T::BaseType>::min() ),
			T maxValue = T( Imath::limits<typename T::BaseType>::max() ),
			unsigned flags = None
		);
		virtual ~CompoundNumericPlug();

		/// Accepts no children following construction.
		virtual bool acceptsChild( ConstGraphComponentPtr potentialChild ) const;

		typename ChildType::Ptr getChild( unsigned i );
		typename ChildType::ConstPtr getChild( unsigned i ) const;	

		T defaultValue() const;
		
		bool hasMinValue() const;
		bool hasMaxValue() const;

		T minValue() const;
		T maxValue() const;
		
		/// Calls setValue for each of the child plugs, passing the components
		/// of value.
		/// \undoable
		void setValue( T value );
		/// Returns the value, calling getValue() on each child plug to compute a component
		/// of the result. This isn't const as it may require a compute and therefore a setValue().
		T getValue();
		
	private :
	
		static const char **childNames();
	
};

typedef CompoundNumericPlug<Imath::V2f> V2fPlug;
typedef CompoundNumericPlug<Imath::V3f> V3fPlug;

typedef CompoundNumericPlug<Imath::V2i> V2iPlug;
typedef CompoundNumericPlug<Imath::V3i> V3iPlug;

typedef CompoundNumericPlug<Imath::Color3f> Color3fPlug;
typedef CompoundNumericPlug<Imath::Color4f> Color4fPlug;

IE_CORE_DECLAREPTR( V2fPlug );
IE_CORE_DECLAREPTR( V3fPlug );
IE_CORE_DECLAREPTR( V2iPlug );
IE_CORE_DECLAREPTR( V3iPlug );
IE_CORE_DECLAREPTR( Color3fPlug );
IE_CORE_DECLAREPTR( Color4fPlug );

} // namespace Gaffer

#endif // GAFFER_COMPOUNDNUMERICPLUG_H