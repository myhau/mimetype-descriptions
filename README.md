# mimetype-descriptions :notebook:
Library that provides localized description of mimetypes (based on shared-mime-info)


### Installation

[![NPM](https://nodei.co/npm/mimetype-descriptions.png?compact=true)](https://npmjs.org/package/mimetype-descriptions)

`npm install mimetype-descriptions`


### Usage
 
```javascript
import mimetype from "mimetype-descriptions" 
// or 
// var mimetype = require("mimetype-descriptions");
 

// lang defaults to "en"
mimetype.description("application/x-desktop");                  // "desktop configuration file"

mimetype.description("text/mathml", "pl");                      // "Dokument MathML"

mimetype.acronym("text/mathml");                                // "MathML"

mimetype.expanded("text/mathml");                               // "Mathematical Markup Language"

mimetype.icon("application/vnd.ms-powerpoint");                 // "x-office-presentation"

mimetype.description("application/vnd.ms-powerpoint", "en_GB"); // "PowerPoint Presentation"

mimetype.full("application/vnd.ms-powerpoint");                 // returns description, acronym, expanded, icon in single object
 /*
 { 
   type: 'application/vnd.ms-powerpoint',
   description: {
      el: 'Παρουσίαση PowerPoint',
      eo: 'PowerPoint-prezentaĵo',
      en: 'PowerPoint presentation',
      oc: 'presentacion PowerPoint',
      ca: 'presentació de PowerPoint',
      it: 'Presentazione PowerPoint',
      cs: 'prezentace PowerPoint',
      ar: 'عرض تقديمي PowerPoint',
      ga: 'láithreoireacht PowerPoint',
      eu: 'PowerPoint aurkezpena',
      gl: 'presentación de PowerPoint',
      id: 'Presentasi PowerPoint',
      es: 'presentación de PowerPoint',
      ru: 'презентация PowerPoint',
      pt: 'apresentação PowerPoint',
      nl: 'PowerPoint-presentatie',
      nn: 'PowerPoint-presentasjon',
      nb: 'PowerPoint-presentasjon',
      tr: 'PowerPoint sunumu',
      lv: 'PowerPoint prezentācija',
      lt: 'PowerPoint pateiktis',
      vi: 'Trình diễn PowerPoint',
      zh_TW: 'PowerPoint 簡報',
      fo: 'PowerPoint framløga',
      ia: 'Presentation PowerPoint',
      en_GB: 'PowerPoint presentation',
      fr: 'présentation PowerPoint',
      bg: 'Презентация — PowerPoint',
      pt_BR: 'Apresentação do PowerPoint',
      hr: 'PowerPoint prezentacija',
      de: 'PowerPoint-Präsentation',
      hu: 'PowerPoint prezentáció',
      fi: 'PowerPoint-esitys',
      da: 'PowerPoint-præsentation',
      ja: 'PowerPoint プレゼンテーション',
      he: 'מצגת PowerPoint',
      ro: 'Prezentare PowerPoint',
      'be@latin': 'Prezentacyja PowerPoint',
      zh_CN: 'Microsoft PowerPoint 演示文稿',
      kk: 'PowerPoint презентациясы',
      sr: 'Пауер Поинт презентација',
      sq: 'Prezantim PowerPoint',
      ko: 'PowerPoint 프레젠테이션',
      sv: 'PowerPoint-presentation',
      sk: 'Prezentácia PowerPoint',
      pl: 'Prezentacja PowerPoint',
      uk: 'презентація PowerPoint',
      sl: 'Predstavitev Microsoft PowerPoint' 
   },
   icon: 'x-office-presentation' 
 }
 */
 
```


### How it works 
It uses [shared-mime-info](https://freedesktop.org/wiki/Software/shared-mime-info/) (`freedesktop.org.xml` file)

