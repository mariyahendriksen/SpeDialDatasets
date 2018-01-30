# SpeDialDatasets

Data from the SpeDial Datasets published in the 2016 LREC paper "The SpeDial Datasets: Datasets for Spoken Dialogue Systems Analytics" by J. Lopes, A. Chorianopoulou, E. Palogiannidi, H. Moniz, A. Abad, K. Louka, E. Iosif and A. Potamianos. Please find the paper with the data description [here](http://www.speech.kth.se/prod/publications/files/4048.pdf). The dataset was collected by the CMU Let's Go bus information system while it was still connected to the Pittsburgh's Port Authority.

Content:

  - `letsgo.2014.lrec.tar.gz`: compressed file will all the data
  - `spdxml.py`: Python class that parses the xml file in SpdXml format (included in the compressed file).
  - `spdxml_letsgo_2014.xml`: Data set in the SpdXml format. Includes all the utterances in written form, annotations (both automatic and manual), dialogue acts, etc (included in the compressed file).
  - `spedxml.xsd`: XSD definition of the SpdXml format (included in the compressed file).

