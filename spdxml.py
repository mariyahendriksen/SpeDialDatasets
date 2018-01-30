# .\spdxml.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:aa9161f93255cb8cc31b5ea585968b6f35fdf1c0
# Generated 2015-08-14 11:43:06.155000 by PyXB version 1.2.4 using Python 2.7.6.final.0
# Namespace spedial

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:dd44be0f-4268-11e5-ba80-f8b156a007f6')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('spedial', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {spedial}attributeTypes
class attributeTypes (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'attributeTypes')
    _XSDLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 269, 2)
    _Documentation = None
attributeTypes._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=attributeTypes, enum_prefix=None)
attributeTypes.integer = attributeTypes._CF_enumeration.addEnumeration(unicode_value='integer', tag='integer')
attributeTypes.float = attributeTypes._CF_enumeration.addEnumeration(unicode_value='float', tag='float')
attributeTypes.boolean = attributeTypes._CF_enumeration.addEnumeration(unicode_value='boolean', tag='boolean')
attributeTypes.string = attributeTypes._CF_enumeration.addEnumeration(unicode_value='string', tag='string')
attributeTypes._InitializeFacetMap(attributeTypes._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'attributeTypes', attributeTypes)

# Complex type {spedial}corpora with content type ELEMENT_ONLY
class corpora_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {spedial}corpora with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'corpora')
    _XSDLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 21, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {spedial}corpus uses Python identifier corpus
    __corpus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'corpus'), 'corpus', '__spedial_corpora__spedialcorpus', True, pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 23, 6), )

    
    corpus = property(__corpus.value, __corpus.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__spedial_corpora__id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 26, 4)
    __id._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 26, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute schema-version uses Python identifier schema_version
    __schema_version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'schema-version'), 'schema_version', '__spedial_corpora__schema_version', pyxb.binding.datatypes.string, fixed=True, unicode_default='1.0', required=True)
    __schema_version._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 28, 4)
    __schema_version._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 28, 4)
    
    schema_version = property(__schema_version.value, __schema_version.set, None, None)

    _ElementMap.update({
        __corpus.name() : __corpus
    })
    _AttributeMap.update({
        __id.name() : __id,
        __schema_version.name() : __schema_version
    })
Namespace.addCategoryObject('typeBinding', 'corpora', corpora_)


# Complex type {spedial}corpus with content type ELEMENT_ONLY
class corpus_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {spedial}corpus with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'corpus')
    _XSDLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 32, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {spedial}dialogue uses Python identifier dialogue
    __dialogue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dialogue'), 'dialogue', '__spedial_corpus__spedialdialogue', True, pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 34, 6), )

    
    dialogue = property(__dialogue.value, __dialogue.set, None, None)

    
    # Element {spedial}attributes uses Python identifier attributes
    __attributes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'attributes'), 'attributes', '__spedial_corpus__spedialattributes', False, pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 36, 6), )

    
    attributes = property(__attributes.value, __attributes.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__spedial_corpus__id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 39, 4)
    __id._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 39, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute schema-version uses Python identifier schema_version
    __schema_version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'schema-version'), 'schema_version', '__spedial_corpus__schema_version', pyxb.binding.datatypes.string, fixed=True, unicode_default='1.0', required=True)
    __schema_version._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 41, 4)
    __schema_version._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 41, 4)
    
    schema_version = property(__schema_version.value, __schema_version.set, None, None)

    _ElementMap.update({
        __dialogue.name() : __dialogue,
        __attributes.name() : __attributes
    })
    _AttributeMap.update({
        __id.name() : __id,
        __schema_version.name() : __schema_version
    })
Namespace.addCategoryObject('typeBinding', 'corpus', corpus_)


# Complex type {spedial}dialogue with content type ELEMENT_ONLY
class dialogue_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {spedial}dialogue with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'dialogue')
    _XSDLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 45, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {spedial}annotators uses Python identifier annotators
    __annotators = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'annotators'), 'annotators', '__spedial_dialogue__spedialannotators', False, pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 48, 6), )

    
    annotators = property(__annotators.value, __annotators.set, None, None)

    
    # Element {spedial}attributes uses Python identifier attributes
    __attributes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'attributes'), 'attributes', '__spedial_dialogue__spedialattributes', False, pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 51, 6), )

    
    attributes = property(__attributes.value, __attributes.set, None, None)

    
    # Element {spedial}exchanges uses Python identifier exchanges
    __exchanges = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'exchanges'), 'exchanges', '__spedial_dialogue__spedialexchanges', False, pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 54, 6), )

    
    exchanges = property(__exchanges.value, __exchanges.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__spedial_dialogue__id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 57, 4)
    __id._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 57, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute date uses Python identifier date
    __date = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'date'), 'date', '__spedial_dialogue__date', pyxb.binding.datatypes.date)
    __date._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 59, 4)
    __date._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 59, 4)
    
    date = property(__date.value, __date.set, None, None)

    
    # Attribute start-time uses Python identifier start_time
    __start_time = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'start-time'), 'start_time', '__spedial_dialogue__start_time', pyxb.binding.datatypes.time)
    __start_time._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 61, 4)
    __start_time._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 61, 4)
    
    start_time = property(__start_time.value, __start_time.set, None, None)

    
    # Attribute end-time uses Python identifier end_time
    __end_time = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'end-time'), 'end_time', '__spedial_dialogue__end_time', pyxb.binding.datatypes.time)
    __end_time._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 63, 4)
    __end_time._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 63, 4)
    
    end_time = property(__end_time.value, __end_time.set, None, None)

    
    # Attribute schema-version uses Python identifier schema_version
    __schema_version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'schema-version'), 'schema_version', '__spedial_dialogue__schema_version', pyxb.binding.datatypes.string, fixed=True, unicode_default='1.0', required=True)
    __schema_version._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 65, 4)
    __schema_version._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 65, 4)
    
    schema_version = property(__schema_version.value, __schema_version.set, None, None)

    _ElementMap.update({
        __annotators.name() : __annotators,
        __attributes.name() : __attributes,
        __exchanges.name() : __exchanges
    })
    _AttributeMap.update({
        __id.name() : __id,
        __date.name() : __date,
        __start_time.name() : __start_time,
        __end_time.name() : __end_time,
        __schema_version.name() : __schema_version
    })
Namespace.addCategoryObject('typeBinding', 'dialogue', dialogue_)


# Complex type {spedial}annotator-list with content type ELEMENT_ONLY
class annotator_list (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {spedial}annotator-list with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'annotator-list')
    _XSDLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 69, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {spedial}annotator uses Python identifier annotator
    __annotator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'annotator'), 'annotator', '__spedial_annotator_list_spedialannotator', True, pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 71, 6), )

    
    annotator = property(__annotator.value, __annotator.set, None, None)

    _ElementMap.update({
        __annotator.name() : __annotator
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'annotator-list', annotator_list)


# Complex type {spedial}annotator with content type SIMPLE
class annotator (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {spedial}annotator with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'annotator')
    _XSDLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 75, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__spedial_annotator_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 79, 8)
    __id._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 79, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__spedial_annotator_version', pyxb.binding.datatypes.string, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 81, 8)
    __version._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 81, 8)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute date uses Python identifier date
    __date = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'date'), 'date', '__spedial_annotator_date', pyxb.binding.datatypes.date, required=True)
    __date._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 83, 8)
    __date._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 83, 8)
    
    date = property(__date.value, __date.set, None, None)

    
    # Attribute time uses Python identifier time
    __time = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'time'), 'time', '__spedial_annotator_time', pyxb.binding.datatypes.time, required=True)
    __time._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 85, 8)
    __time._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 85, 8)
    
    time = property(__time.value, __time.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __version.name() : __version,
        __date.name() : __date,
        __time.name() : __time
    })
Namespace.addCategoryObject('typeBinding', 'annotator', annotator)


# Complex type {spedial}attribute-list with content type ELEMENT_ONLY
class attribute_list (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {spedial}attribute-list with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'attribute-list')
    _XSDLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 90, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {spedial}attribute uses Python identifier attribute
    __attribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'attribute'), 'attribute', '__spedial_attribute_list_spedialattribute', True, pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 92, 6), )

    
    attribute = property(__attribute.value, __attribute.set, None, None)

    _ElementMap.update({
        __attribute.name() : __attribute
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'attribute-list', attribute_list)


# Complex type {spedial}turn-exchange-list with content type ELEMENT_ONLY
class turn_exchange_list (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {spedial}turn-exchange-list with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'turn-exchange-list')
    _XSDLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 112, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {spedial}exchange uses Python identifier exchange
    __exchange = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'exchange'), 'exchange', '__spedial_turn_exchange_list_spedialexchange', True, pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 114, 6), )

    
    exchange = property(__exchange.value, __exchange.set, None, None)

    _ElementMap.update({
        __exchange.name() : __exchange
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'turn-exchange-list', turn_exchange_list)


# Complex type {spedial}exchange with content type ELEMENT_ONLY
class exchange (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {spedial}exchange with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'exchange')
    _XSDLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 119, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {spedial}attributes uses Python identifier attributes
    __attributes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'attributes'), 'attributes', '__spedial_exchange_spedialattributes', False, pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 122, 6), )

    
    attributes = property(__attributes.value, __attributes.set, None, None)

    
    # Element {spedial}system uses Python identifier system
    __system = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'system'), 'system', '__spedial_exchange_spedialsystem', False, pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 124, 6), )

    
    system = property(__system.value, __system.set, None, None)

    
    # Element {spedial}user uses Python identifier user
    __user = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'user'), 'user', '__spedial_exchange_spedialuser', False, pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 125, 6), )

    
    user = property(__user.value, __user.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__spedial_exchange_id', pyxb.binding.datatypes.integer, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 128, 4)
    __id._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 128, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute start-time uses Python identifier start_time
    __start_time = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'start-time'), 'start_time', '__spedial_exchange_start_time', pyxb.binding.datatypes.time)
    __start_time._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 130, 4)
    __start_time._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 130, 4)
    
    start_time = property(__start_time.value, __start_time.set, None, None)

    
    # Attribute end-time uses Python identifier end_time
    __end_time = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'end-time'), 'end_time', '__spedial_exchange_end_time', pyxb.binding.datatypes.time)
    __end_time._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 132, 4)
    __end_time._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 132, 4)
    
    end_time = property(__end_time.value, __end_time.set, None, None)

    _ElementMap.update({
        __attributes.name() : __attributes,
        __system.name() : __system,
        __user.name() : __user
    })
    _AttributeMap.update({
        __id.name() : __id,
        __start_time.name() : __start_time,
        __end_time.name() : __end_time
    })
Namespace.addCategoryObject('typeBinding', 'exchange', exchange)


# Complex type {spedial}system-turn with content type ELEMENT_ONLY
class system_turn (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {spedial}system-turn with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'system-turn')
    _XSDLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 135, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {spedial}prompt uses Python identifier prompt
    __prompt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'prompt'), 'prompt', '__spedial_system_turn_spedialprompt', False, pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 138, 6), )

    
    prompt = property(__prompt.value, __prompt.set, None, None)

    
    # Element {spedial}semantics uses Python identifier semantics
    __semantics = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'semantics'), 'semantics', '__spedial_system_turn_spedialsemantics', False, pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 140, 6), )

    
    semantics = property(__semantics.value, __semantics.set, None, None)

    
    # Element {spedial}attributes uses Python identifier attributes
    __attributes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'attributes'), 'attributes', '__spedial_system_turn_spedialattributes', False, pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 142, 6), )

    
    attributes = property(__attributes.value, __attributes.set, None, None)

    
    # Attribute start-time uses Python identifier start_time
    __start_time = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'start-time'), 'start_time', '__spedial_system_turn_start_time', pyxb.binding.datatypes.time)
    __start_time._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 145, 4)
    __start_time._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 145, 4)
    
    start_time = property(__start_time.value, __start_time.set, None, None)

    
    # Attribute end-time uses Python identifier end_time
    __end_time = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'end-time'), 'end_time', '__spedial_system_turn_end_time', pyxb.binding.datatypes.time)
    __end_time._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 147, 4)
    __end_time._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 147, 4)
    
    end_time = property(__end_time.value, __end_time.set, None, None)

    _ElementMap.update({
        __prompt.name() : __prompt,
        __semantics.name() : __semantics,
        __attributes.name() : __attributes
    })
    _AttributeMap.update({
        __start_time.name() : __start_time,
        __end_time.name() : __end_time
    })
Namespace.addCategoryObject('typeBinding', 'system-turn', system_turn)


# Complex type {spedial}user-turn with content type ELEMENT_ONLY
class user_turn (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {spedial}user-turn with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'user-turn')
    _XSDLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 150, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {spedial}recognition-results uses Python identifier recognition_results
    __recognition_results = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'recognition-results'), 'recognition_results', '__spedial_user_turn_spedialrecognition_results', False, pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 153, 6), )

    
    recognition_results = property(__recognition_results.value, __recognition_results.set, None, None)

    
    # Element {spedial}transcriptions uses Python identifier transcriptions
    __transcriptions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'transcriptions'), 'transcriptions', '__spedial_user_turn_spedialtranscriptions', False, pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 156, 6), )

    
    transcriptions = property(__transcriptions.value, __transcriptions.set, None, None)

    
    # Element {spedial}audio uses Python identifier audio
    __audio = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'audio'), 'audio', '__spedial_user_turn_spedialaudio', False, pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 159, 6), )

    
    audio = property(__audio.value, __audio.set, None, None)

    
    # Element {spedial}attributes uses Python identifier attributes
    __attributes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'attributes'), 'attributes', '__spedial_user_turn_spedialattributes', False, pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 162, 6), )

    
    attributes = property(__attributes.value, __attributes.set, None, None)

    
    # Attribute start-time uses Python identifier start_time
    __start_time = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'start-time'), 'start_time', '__spedial_user_turn_start_time', pyxb.binding.datatypes.time)
    __start_time._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 165, 4)
    __start_time._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 165, 4)
    
    start_time = property(__start_time.value, __start_time.set, None, None)

    
    # Attribute end-time uses Python identifier end_time
    __end_time = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'end-time'), 'end_time', '__spedial_user_turn_end_time', pyxb.binding.datatypes.time)
    __end_time._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 167, 4)
    __end_time._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 167, 4)
    
    end_time = property(__end_time.value, __end_time.set, None, None)

    _ElementMap.update({
        __recognition_results.name() : __recognition_results,
        __transcriptions.name() : __transcriptions,
        __audio.name() : __audio,
        __attributes.name() : __attributes
    })
    _AttributeMap.update({
        __start_time.name() : __start_time,
        __end_time.name() : __end_time
    })
Namespace.addCategoryObject('typeBinding', 'user-turn', user_turn)


# Complex type {spedial}recognition-hypothesis-list with content type ELEMENT_ONLY
class recognition_hypothesis_list (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {spedial}recognition-hypothesis-list with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'recognition-hypothesis-list')
    _XSDLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 170, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {spedial}hypothesis uses Python identifier hypothesis
    __hypothesis = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hypothesis'), 'hypothesis', '__spedial_recognition_hypothesis_list_spedialhypothesis', True, pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 173, 6), )

    
    hypothesis = property(__hypothesis.value, __hypothesis.set, None, None)

    
    # Element {spedial}semantics uses Python identifier semantics
    __semantics = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'semantics'), 'semantics', '__spedial_recognition_hypothesis_list_spedialsemantics', False, pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 176, 6), )

    
    semantics = property(__semantics.value, __semantics.set, None, None)

    _ElementMap.update({
        __hypothesis.name() : __hypothesis,
        __semantics.name() : __semantics
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'recognition-hypothesis-list', recognition_hypothesis_list)


# Complex type {spedial}recognition-hypothesis with content type SIMPLE
class recognition_hypothesis (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {spedial}recognition-hypothesis with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'recognition-hypothesis')
    _XSDLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 180, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute confidence uses Python identifier confidence
    __confidence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'confidence'), 'confidence', '__spedial_recognition_hypothesis_confidence', pyxb.binding.datatypes.float)
    __confidence._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 184, 8)
    __confidence._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 184, 8)
    
    confidence = property(__confidence.value, __confidence.set, None, None)

    
    # Attribute rank uses Python identifier rank
    __rank = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rank'), 'rank', '__spedial_recognition_hypothesis_rank', pyxb.binding.datatypes.integer)
    __rank._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 186, 8)
    __rank._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 186, 8)
    
    rank = property(__rank.value, __rank.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__spedial_recognition_hypothesis_id', pyxb.binding.datatypes.integer)
    __id._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 188, 8)
    __id._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 188, 8)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __confidence.name() : __confidence,
        __rank.name() : __rank,
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', 'recognition-hypothesis', recognition_hypothesis)


# Complex type {spedial}semantic-hypothesis-list with content type ELEMENT_ONLY
class semantic_hypothesis_list (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {spedial}semantic-hypothesis-list with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'semantic-hypothesis-list')
    _XSDLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 193, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {spedial}hypothesis uses Python identifier hypothesis
    __hypothesis = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hypothesis'), 'hypothesis', '__spedial_semantic_hypothesis_list_spedialhypothesis', True, pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 196, 6), )

    
    hypothesis = property(__hypothesis.value, __hypothesis.set, None, None)

    _ElementMap.update({
        __hypothesis.name() : __hypothesis
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'semantic-hypothesis-list', semantic_hypothesis_list)


# Complex type {spedial}transcription-list with content type ELEMENT_ONLY
class transcription_list (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {spedial}transcription-list with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'transcription-list')
    _XSDLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 200, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {spedial}transcription uses Python identifier transcription
    __transcription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'transcription'), 'transcription', '__spedial_transcription_list_spedialtranscription', True, pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 203, 6), )

    
    transcription = property(__transcription.value, __transcription.set, None, None)

    
    # Element {spedial}semantics uses Python identifier semantics
    __semantics = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'semantics'), 'semantics', '__spedial_transcription_list_spedialsemantics', False, pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 206, 6), )

    
    semantics = property(__semantics.value, __semantics.set, None, None)

    _ElementMap.update({
        __transcription.name() : __transcription,
        __semantics.name() : __semantics
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'transcription-list', transcription_list)


# Complex type {spedial}transcription with content type SIMPLE
class transcription (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {spedial}transcription with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'transcription')
    _XSDLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 211, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute confidence uses Python identifier confidence
    __confidence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'confidence'), 'confidence', '__spedial_transcription_confidence', pyxb.binding.datatypes.float)
    __confidence._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 215, 8)
    __confidence._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 215, 8)
    
    confidence = property(__confidence.value, __confidence.set, None, None)

    
    # Attribute rank uses Python identifier rank
    __rank = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rank'), 'rank', '__spedial_transcription_rank', pyxb.binding.datatypes.integer)
    __rank._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 217, 8)
    __rank._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 217, 8)
    
    rank = property(__rank.value, __rank.set, None, None)

    
    # Attribute date uses Python identifier date
    __date = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'date'), 'date', '__spedial_transcription_date', pyxb.binding.datatypes.date)
    __date._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 219, 8)
    __date._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 219, 8)
    
    date = property(__date.value, __date.set, None, None)

    
    # Attribute time uses Python identifier time
    __time = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'time'), 'time', '__spedial_transcription_time', pyxb.binding.datatypes.time)
    __time._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 221, 8)
    __time._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 221, 8)
    
    time = property(__time.value, __time.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __confidence.name() : __confidence,
        __rank.name() : __rank,
        __date.name() : __date,
        __time.name() : __time
    })
Namespace.addCategoryObject('typeBinding', 'transcription', transcription)


# Complex type {spedial}semantic-hypothesis with content type ELEMENT_ONLY
class semantic_hypothesis (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {spedial}semantic-hypothesis with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'semantic-hypothesis')
    _XSDLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 226, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {spedial}original uses Python identifier original
    __original = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'original'), 'original', '__spedial_semantic_hypothesis_spedialoriginal', False, pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 230, 6), )

    
    original = property(__original.value, __original.set, None, None)

    
    # Element {spedial}semantic-concept uses Python identifier semantic_concept
    __semantic_concept = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'semantic-concept'), 'semantic_concept', '__spedial_semantic_hypothesis_spedialsemantic_concept', True, pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 234, 6), )

    
    semantic_concept = property(__semantic_concept.value, __semantic_concept.set, None, None)

    
    # Attribute confidence uses Python identifier confidence
    __confidence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'confidence'), 'confidence', '__spedial_semantic_hypothesis_confidence', pyxb.binding.datatypes.float)
    __confidence._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 239, 4)
    __confidence._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 239, 4)
    
    confidence = property(__confidence.value, __confidence.set, None, None)

    
    # Attribute rank uses Python identifier rank
    __rank = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rank'), 'rank', '__spedial_semantic_hypothesis_rank', pyxb.binding.datatypes.integer)
    __rank._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 241, 4)
    __rank._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 241, 4)
    
    rank = property(__rank.value, __rank.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__spedial_semantic_hypothesis_id', pyxb.binding.datatypes.integer)
    __id._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 243, 4)
    __id._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 243, 4)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __original.name() : __original,
        __semantic_concept.name() : __semantic_concept
    })
    _AttributeMap.update({
        __confidence.name() : __confidence,
        __rank.name() : __rank,
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', 'semantic-hypothesis', semantic_hypothesis)


# Complex type {spedial}semantic-concept with content type SIMPLE
class semantic_concept (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {spedial}semantic-concept with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'semantic-concept')
    _XSDLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 246, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute confidence uses Python identifier confidence
    __confidence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'confidence'), 'confidence', '__spedial_semantic_concept_confidence', pyxb.binding.datatypes.float)
    __confidence._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 250, 9)
    __confidence._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 250, 9)
    
    confidence = property(__confidence.value, __confidence.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __confidence.name() : __confidence
    })
Namespace.addCategoryObject('typeBinding', 'semantic-concept', semantic_concept)


# Complex type {spedial}audio with content type SIMPLE
class audio (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {spedial}audio with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'audio')
    _XSDLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 256, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute url uses Python identifier url
    __url = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'url'), 'url', '__spedial_audio_url', pyxb.binding.datatypes.anyURI)
    __url._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 259, 9)
    __url._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 259, 9)
    
    url = property(__url.value, __url.set, None, None)

    
    # Attribute start-time uses Python identifier start_time
    __start_time = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'start-time'), 'start_time', '__spedial_audio_start_time', pyxb.binding.datatypes.time)
    __start_time._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 261, 9)
    __start_time._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 261, 9)
    
    start_time = property(__start_time.value, __start_time.set, None, None)

    
    # Attribute end-time uses Python identifier end_time
    __end_time = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'end-time'), 'end_time', '__spedial_audio_end_time', pyxb.binding.datatypes.time)
    __end_time._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 263, 9)
    __end_time._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 263, 9)
    
    end_time = property(__end_time.value, __end_time.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __url.name() : __url,
        __start_time.name() : __start_time,
        __end_time.name() : __end_time
    })
Namespace.addCategoryObject('typeBinding', 'audio', audio)


# Complex type {spedial}attribute with content type SIMPLE
class attribute (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {spedial}attribute with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'attribute')
    _XSDLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 96, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__spedial_attribute_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 100, 8)
    __name._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 100, 8)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__spedial_attribute_type', attributeTypes, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 102, 8)
    __type._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 102, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute category uses Python identifier category
    __category = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'category'), 'category', '__spedial_attribute_category', pyxb.binding.datatypes.string)
    __category._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 105, 8)
    __category._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 105, 8)
    
    category = property(__category.value, __category.set, None, None)

    
    # Attribute annotator uses Python identifier annotator
    __annotator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'annotator'), 'annotator', '__spedial_attribute_annotator', pyxb.binding.datatypes.string)
    __annotator._DeclarationLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 107, 8)
    __annotator._UseLocation = pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 107, 8)
    
    annotator = property(__annotator.value, __annotator.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __type.name() : __type,
        __category.name() : __category,
        __annotator.name() : __annotator
    })
Namespace.addCategoryObject('typeBinding', 'attribute', attribute)


corpora = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'corpora'), corpora_, location=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 16, 2))
Namespace.addCategoryObject('elementBinding', corpora.name().localName(), corpora)

corpus = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'corpus'), corpus_, location=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 17, 2))
Namespace.addCategoryObject('elementBinding', corpus.name().localName(), corpus)

dialogue = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dialogue'), dialogue_, location=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 18, 2))
Namespace.addCategoryObject('elementBinding', dialogue.name().localName(), dialogue)



corpora_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'corpus'), corpus_, scope=corpora_, location=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 23, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(corpora_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'corpus')), pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 23, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
corpora_._Automaton = _BuildAutomaton()




corpus_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dialogue'), dialogue_, scope=corpus_, location=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 34, 6)))

corpus_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'attributes'), attribute_list, scope=corpus_, location=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 36, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 36, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(corpus_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dialogue')), pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 34, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(corpus_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributes')), pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 36, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
corpus_._Automaton = _BuildAutomaton_()




dialogue_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'annotators'), annotator_list, scope=dialogue_, location=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 48, 6)))

dialogue_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'attributes'), attribute_list, scope=dialogue_, location=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 51, 6)))

dialogue_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'exchanges'), turn_exchange_list, scope=dialogue_, location=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 54, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 48, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 51, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 54, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(dialogue_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'annotators')), pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 48, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(dialogue_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributes')), pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 51, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(dialogue_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'exchanges')), pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 54, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
dialogue_._Automaton = _BuildAutomaton_2()




annotator_list._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'annotator'), annotator, scope=annotator_list, location=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 71, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 71, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(annotator_list._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'annotator')), pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 71, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
annotator_list._Automaton = _BuildAutomaton_3()




attribute_list._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'attribute'), attribute, scope=attribute_list, location=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 92, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 92, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(attribute_list._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attribute')), pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 92, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
attribute_list._Automaton = _BuildAutomaton_4()




turn_exchange_list._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'exchange'), exchange, scope=turn_exchange_list, location=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 114, 6)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 114, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(turn_exchange_list._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'exchange')), pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 114, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
turn_exchange_list._Automaton = _BuildAutomaton_5()




exchange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'attributes'), attribute_list, scope=exchange, location=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 122, 6)))

exchange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'system'), system_turn, scope=exchange, location=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 124, 6)))

exchange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'user'), user_turn, scope=exchange, location=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 125, 6)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 122, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 124, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 125, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(exchange._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributes')), pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 122, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(exchange._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'system')), pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 124, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(exchange._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'user')), pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 125, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
exchange._Automaton = _BuildAutomaton_6()




system_turn._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'prompt'), pyxb.binding.datatypes.string, scope=system_turn, location=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 138, 6)))

system_turn._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'semantics'), semantic_hypothesis_list, scope=system_turn, location=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 140, 6)))

system_turn._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'attributes'), attribute_list, scope=system_turn, location=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 142, 6)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 138, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 140, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 142, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(system_turn._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'prompt')), pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 138, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(system_turn._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'semantics')), pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 140, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(system_turn._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributes')), pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 142, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
system_turn._Automaton = _BuildAutomaton_7()




user_turn._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'recognition-results'), recognition_hypothesis_list, scope=user_turn, location=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 153, 6)))

user_turn._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transcriptions'), transcription_list, scope=user_turn, location=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 156, 6)))

user_turn._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'audio'), audio, scope=user_turn, location=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 159, 6)))

user_turn._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'attributes'), attribute_list, scope=user_turn, location=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 162, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 153, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 156, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 159, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 162, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(user_turn._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'recognition-results')), pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 153, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(user_turn._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transcriptions')), pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 156, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(user_turn._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'audio')), pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 159, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(user_turn._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributes')), pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 162, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
user_turn._Automaton = _BuildAutomaton_8()




recognition_hypothesis_list._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hypothesis'), recognition_hypothesis, scope=recognition_hypothesis_list, location=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 173, 6)))

recognition_hypothesis_list._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'semantics'), semantic_hypothesis_list, scope=recognition_hypothesis_list, location=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 176, 6)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 176, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(recognition_hypothesis_list._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hypothesis')), pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 173, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(recognition_hypothesis_list._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'semantics')), pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 176, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
recognition_hypothesis_list._Automaton = _BuildAutomaton_9()




semantic_hypothesis_list._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hypothesis'), semantic_hypothesis, scope=semantic_hypothesis_list, location=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 196, 6)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(semantic_hypothesis_list._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hypothesis')), pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 196, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
semantic_hypothesis_list._Automaton = _BuildAutomaton_10()




transcription_list._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transcription'), transcription, scope=transcription_list, location=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 203, 6)))

transcription_list._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'semantics'), semantic_hypothesis_list, scope=transcription_list, location=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 206, 6)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 206, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(transcription_list._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transcription')), pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 203, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(transcription_list._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'semantics')), pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 206, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
transcription_list._Automaton = _BuildAutomaton_11()




semantic_hypothesis._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'original'), pyxb.binding.datatypes.string, scope=semantic_hypothesis, location=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 230, 6)))

semantic_hypothesis._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'semantic-concept'), semantic_concept, scope=semantic_hypothesis, location=pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 234, 6)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(semantic_hypothesis._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'original')), pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 230, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(semantic_hypothesis._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'semantic-concept')), pyxb.utils.utility.Location('c:\\SVN\\trunk\\LogParser\\xml\\spedxml.xsd', 234, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
semantic_hypothesis._Automaton = _BuildAutomaton_12()

