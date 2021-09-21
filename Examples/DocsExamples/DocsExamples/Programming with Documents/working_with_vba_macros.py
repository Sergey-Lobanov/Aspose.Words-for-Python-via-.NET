import unittest
import os
import sys

base_dir = os.path.abspath(os.curdir) + "/"
base_dir = base_dir[:base_dir.find("Aspose.Words-for-Python-via-.NET")]
base_dir = base_dir + "Aspose.Words-for-Python-via-.NET/Examples/DocsExamples/DocsExamples"
sys.path.insert(0, base_dir)

import docs_examples_base as docs_base

import aspose.words as aw

class WorkingWithVba(docs_base.DocsExamplesBase):

    
    def test_create_vba_project(self) :
        
        #ExStart:CreateVbaProject
        doc = aw.Document()

        project = aw.vba.VbaProject()
        project.name = "AsposeProject"
        doc.vba_project = project

        # Create a new module and specify a macro source code.
        module = aw.vba.VbaModule()
        module.name = "AsposeModule"
        module.type = aw.vba.VbaModuleType.PROCEDURAL_MODULE
        module.source_code = "New source code"

        # Add module to the VBA project.
        doc.vba_project.modules.add(module)

        doc.save(docs_base.artifacts_dir + "WorkingWithVba.create_vba_project.docm")
        #ExEnd:CreateVbaProject
        

    def test_read_vba_macros(self) :
        
        #ExStart:ReadVbaMacros
        doc = aw.Document(docs_base.my_dir + "VBA project.docm")

        if (doc.vba_project != None) :
            for module in doc.vba_project.modules :
                print(module.source_code)
            
        #ExEnd:ReadVbaMacros
        

    def test_modify_vba_macros(self) :
        
        #ExStart:ModifyVbaMacros
        doc = aw.Document(docs_base.my_dir + "VBA project.docm")

        project = doc.vba_project

        newSourceCode = "Test change source code"
        project.modules[0].source_code = newSourceCode
        #ExEnd:ModifyVbaMacros
            
        doc.save(docs_base.artifacts_dir + "WorkingWithVba.modify_vba_macros.docm")
        #ExEnd:ModifyVbaMacros
        

    def test_clone_vba_project(self) :
        
        #ExStart:CloneVbaProject
        doc = aw.Document(docs_base.my_dir + "VBA project.docm")
        destDoc = aw.Document()
        destDoc.vba_project = doc.vba_project.clone() 

        destDoc.save(docs_base.artifacts_dir + "WorkingWithVba.clone_vba_project.docm")
        #ExEnd:CloneVbaProject
        

    def test_clone_vba_module(self) :
        
        #ExStart:CloneVbaModule
        doc = aw.Document(docs_base.my_dir + "VBA project.docm")
        destDoc = aw.Document()
        destDoc.vba_project = aw.vba.VbaProject() 
            
        copyModule = doc.vba_project.modules.get_ny_name("Module1").clone()
        destDoc.vba_project.modules.add(copyModule)

        destDoc.save(docs_base.artifacts_dir + "WorkingWithVba.clone_vba_module.docm")
        #ExEnd:CloneVbaModule
        

    def test_remove_broken_ref(self) :
        
        #ExStart:RemoveReferenceFromCollectionOfReferences
        doc = aw.Document(docs_base.my_dir + "VBA project.docm")

        # Find and remove the reference with some LibId path.
        brokenPath = "brokenPath.dll"
        references = doc.vba_project.references
        for i in range(references.count - 1, 0) :
            
            reference = doc.vba_project.references.element_at(i)

            path = get_lib_id_path(reference)
            if (path == brokenPath) :
                references.remove_at(i)
            

        doc.save(docs_base.artifacts_dir + "WorkingWithVba.remove_broken_ref.docm")
        #ExEnd:RemoveReferenceFromCollectionOfReferences
        
    #ExStart:GetLibIdAndReferencePath
    # <summary>
    # Returns string representing LibId path of a specified reference. 
    # </summary>
    def get_lib_id_path(self, reference) :
        
        if reference.type == aw.vba.VbaReferenceType.REGISTERED or reference.type == aw.vba.VbaReferenceType.ORIGINAL or reference.type == aw.vba.VbaReferenceType.CONTROL :
            return self.get_lib_id_reference_path(reference.lib_id)
        elif reference.type == aw.vba.VbaReferenceType.PROJECT :
            return self.get_lib_id_project_path(reference.lib_id)
        else :
            raise RuntimeError()


    # <summary>
    # Returns path from a specified identifier of an Automation type library.
    # </summary>
    # <remarks>
    # Please see details for the syntax at [MS-OVBA], 2.1.1.8 LibidReference. 
    # </remarks>
    @staticmethod
    def get_lib_id_reference_path(libIdReference : str) :
        
        if (libIdReference != None) :
            
            refParts = libIdReference.split('#')
            if (refParts.length > 3) :
                return refParts[3]
            
        return ""
        

    # <summary>
    # Returns path from a specified identifier of an Automation type library.
    # </summary>
    # <remarks>
    # Please see details for the syntax at [MS-OVBA], 2.1.1.12 ProjectReference. 
    # </remarks>
    @staticmethod
    def get_lib_id_project_path(libIdProject : str) :
        
        if (libIdProject != None) :
           return libIdProject.substring(3) 
           
        return ""
        
    #ExEnd:GetLibIdAndReferencePath
    

if __name__ == '__main__':
    unittest.main()