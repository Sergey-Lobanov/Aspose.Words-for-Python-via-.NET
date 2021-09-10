import unittest
import os
import sys

base_dir = os.path.abspath(os.curdir) + "/"
base_dir = base_dir[:base_dir.find("Aspose.Words-for-Python-via-.NET")]
base_dir = base_dir + "Aspose.Words-for-Python-via-.NET/Examples/DocsExamples/DocsExamples"
sys.path.insert(0, base_dir)
print(base_dir)

import docs_examples_base as docs_base

import aspose.words as aw

class BaseConversions(docs_base.DocsExamplesBase):

    def test_doc_to_docx(self) :
        
        #ExStart:LoadAndSave
        #ExStart:OpenDocument
        doc = aw.Document(docs_base.my_dir + "Document.doc")
        #ExEnd:OpenDocument

        doc.save(docs_base.artifacts_dir + "BaseConversions.doc_to_docx.docx")
        #ExEnd:LoadAndSave
        
    @unittest.skip("Streams are not supported yet.)")
    def test_docx_to_rtf(self) :
         print("not supported yet")
#        #ExStart:LoadAndSaveToStream 
#        #ExStart:OpeningFromStream
#        # Read only access is enough for Aspose.words to load a document.
#        Stream stream = File.open_read(docs_base.my_dir + "Document.docx")
#
#        doc = aw.Document(stream)
#        # You can close the stream now, it is no longer needed because the document is in memory.
#        stream.close()
#        #ExEnd:OpeningFromStream 
#
#        # ... do something with the document.
#
#        # Convert the document to a different format and save to stream.
#        MemoryStream dstStream = new MemoryStream()
#        doc.save(dstStream, SaveFormat.rtf)
#
#        # Rewind the stream position back to zero so it is ready for the next reader.
#        dstStream.position = 0
#        #ExEnd:LoadAndSaveToStream 
#            
#        File.write_all_bytes(docs_base.artifacts_dir + "BaseConversions.docx_to_rtf.rtf", dstStream.to_array())
        

    def test_docx_to_pdf(self) :
        
        #ExStart:Doc2Pdf
        doc = aw.Document(docs_base.my_dir + "Document.docx")

        doc.save(docs_base.artifacts_dir + "BaseConversions.docx_to_pdf.pdf")
        #ExEnd:Doc2Pdf
        
    @unittest.skip("Streams are not supported yet.)")
    def test_docx_to_byte(self) :
        print("not supported yet") 
#        #ExStart:DocxToByte
#        doc = aw.Document(docs_base.my_dir + "Document.docx")
#
#        MemoryStream outStream = new MemoryStream()
#        doc.save(outStream, SaveFormat.docx)
#
#        byte[] docBytes = outStream.to_array()
#        MemoryStream inStream = new MemoryStream(docBytes)
#
#        Document docFromBytes = new Document(inStream)
#        #ExEnd:DocxToByte
        

    def test_docx_to_epub(self) :
        
        #ExStart:DocxToEpub
        doc = aw.Document(docs_base.my_dir + "Document.docx")

        doc.save(docs_base.artifacts_dir + "BaseConversions.docx_to_epub.epub")
        #ExEnd:DocxToEpub
        

    @unittest.skip("Streams are not supported yet.)")
    def test_docx_to_mhtml_and_sending_email(self) :
        print("not supported yet")
#        #ExStart:DocxToMhtmlAndSendingEmail
#        doc = aw.Document(docs_base.my_dir + "Document.docx")
#
#        Stream stream = new MemoryStream()
#        doc.save(stream, SaveFormat.mhtml)
#
#        # Rewind the stream to the beginning so Aspose.email can read it.
#        stream.position = 0
#
#        # Create an Aspose.network MIME email message from the stream.
#        MailMessage message = MailMessage.load(stream, new MhtmlLoadOptions())
#        message.from = "your_from@email.com"
#        message.to = "your_to@email.com"
#        message.subject = "Aspose.words + Aspose.email MHTML Test Message"
#
#        # Send the message using Aspose.email.
#        SmtpClient client = new SmtpClient()
#        client.host = "your_smtp.com"
#        client.send(message)
#        #ExEnd:DocxToMhtmlAndSendingEmail
        

    def test_docx_to_markdown(self) :
        
        #ExStart:SaveToMarkdownDocument
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        builder.writeln("Some text!")

        doc.save(docs_base.artifacts_dir + "BaseConversions.docx_to_markdown.md")
        #ExEnd:SaveToMarkdownDocument
        

    def test_docx_to_txt(self) :
        
        #ExStart:DocxToTxt
        doc = aw.Document(docs_base.my_dir + "Document.docx")

        doc.save(docs_base.artifacts_dir + "BaseConversions.docx_to_txt.txt")
        #ExEnd:DocxToTxt
        

    def test_txt_to_docx(self) :
        
        #ExStart:TxtToDocx
        # The encoding of the text file is automatically detected.
        doc = aw.Document(docs_base.my_dir + "English text.txt")

        doc.save(docs_base.artifacts_dir + "BaseConversions.txt_to_docx.docx")
        #ExEnd:TxtToDocx
        

    def test_pdf_to_jpeg(self) :
        
        #ExStart:PdfToJpeg
        doc = aw.Document(docs_base.my_dir + "Pdf Document.pdf")

        doc.save(docs_base.artifacts_dir + "BaseConversions.pdf_to_jpeg.jpeg")
        #ExEnd:PdfToJpeg
        

    def test_pdf_to_docx(self) :
        
        #ExStart:PdfToDocx
        doc = aw.Document(docs_base.my_dir + "Pdf Document.pdf")

        doc.save(docs_base.artifacts_dir + "BaseConversions.pdf_to_docx.docx")
        #ExEnd:PdfToDocx
        

   
if __name__ == '__main__':
    unittest.main()    