vb-incidents
============

Pulling data from Virginia Beach ePro app of police incidents, for testing new ways to display or search that data.

 * Web GUI: https://wwws.vbgov.com/ePRO/MainUI/Incidents/IncidentSearch.aspx
 * API endpoint: https://public.vbgov.com/Secure/service.asmx?op=GetIncidentData
 * Case Number format: YYYY123456. YYYY represents the year (e.g. 2006) followed by a 6-digit number. Do not include spaces or dashes.
 * In root of this repo is output of a single call to the API, in xml format. 
 * API will only return one days worth of data, and only search value is date.

Ideas for Use
=============
 * Charts and stats showing incidents by date, type
 * Maps showing heatmaps by date range, year-over-year, by type, by change
 * Crime prediction
 * Need a data definication. XML is semi-self-documeting but some fields need more detailed descrpition.

Limitations of API
==================
 * Current API limits query to one day per query, of which all incident data for that day is returned.  
It may be necessary to cache the data in a local storage mechanism for more flexable searching and data display.  
 * A single query to the API took up to 6 seconds in testing.
 * Data only goes back to 1/1/2011.
