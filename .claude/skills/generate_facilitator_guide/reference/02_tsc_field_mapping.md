# TSC Field Mapping and Validation

## Purpose

Documents the automatic TSC field mapping and validation logic used to ensure all required fields are populated correctly.

## TSC Code Structure

TSC codes follow the format: `XXX-YYY-ZZZZ-N.N`

- `XXX` - Sector abbreviation (e.g., LOG, ICT, FIN)
- `YYY` - Category code
- `ZZZZ` - Competency code
- `N.N` - Proficiency level (e.g., 1.1, 2.0, 3.1)

## Sector Mapping

The system maps TSC sector abbreviations to full sector names and Skills Framework names:

| Abbreviation | Sector Name | Skills Framework |
|-------------|-------------|------------------|
| LOG | Logistics | Skills Framework for Logistics |
| ICT | Infocomm Technology | Skills Framework for Infocomm Technology |
| FIN | Financial Services | Skills Framework for Financial Services |
| HR | Human Resource | Skills Framework for Human Resource |
| MFG | Manufacturing | Skills Framework for Manufacturing |
| RET | Retail | Skills Framework for Retail |
| SEC | Security | Skills Framework for Security |
| TOU | Tourism | Skills Framework for Tourism |
| HEA | Healthcare | Skills Framework for Healthcare |
| EDU | Education | Skills Framework for Training and Adult Education |
| HAS | Hotel and Accommodation Services | Skills Framework for Hotel and Accommodation Services |
| FBS | Food Services | Skills Framework for Food Services |
| ATT | Attractions | Skills Framework for Attractions |
| TAE | Training and Adult Education | Skills Framework for Training and Adult Education |
| SER | Services | Skills Framework for Services |
| AIR | Air Transport | Skills Framework for Air Transport |
| SEA | Sea Transport | Skills Framework for Sea Transport |
| LND | Land Transport | Skills Framework for Land Transport |
| ENE | Energy and Chemicals | Skills Framework for Energy and Chemicals |
| AER | Aerospace | Skills Framework for Aerospace |
| BIO | Biopharmaceutical Manufacturing | Skills Framework for Biopharmaceutical Manufacturing |
| MED | Media | Skills Framework for Media |
| DES | Design | Skills Framework for Design |
| BCE | Built Environment | Skills Framework for Built Environment |
| MAR | Marine and Offshore | Skills Framework for Marine and Offshore |
| PRE | Precision Engineering | Skills Framework for Precision Engineering |
| WSH | Workplace Safety and Health | Skills Framework for Workplace Safety and Health |
| PUB | Public Service | Skills Framework for Public Service |
| SOC | Social Service | Skills Framework for Social Service |
| EAC | Early Childhood | Skills Framework for Early Childhood |

## Field Validation Logic

The system validates and auto-populates missing fields:

### TSC_Sector_Abbr
```
IF empty:
    IF Skills_Framework derived from sector mapping exists:
        SET to full Skills Framework name
    ELSE IF Skills_Framework from Course Proposal exists:
        SET to that value
    ELSE:
        SET to sector_name OR TSC_Title OR ""
```

### Skills_Framework
```
IF empty:
    SET to Skills Framework name from sector mapping OR sector_name OR ""
```

### TSC_Category
```
IF empty:
    SET to sector_name from mapping OR TSC_Title OR ""
```

### Proficiency_Level
```
IF empty:
    EXTRACT from TSC_Code using regex: /-(\d+)\.\d+$/
    IF found: SET to "Level {extracted_number}"
    ELSE: SET to ""
```

### Proficiency_Description
```
IF empty:
    IF TSC_Description exists:
        SET to TSC_Description
    ELSE IF TSC_Title exists:
        SET to "Apply knowledge and skills in {tsc_title.lower()} to meet organizational and industry requirements."
    ELSE IF Course_Title exists:
        SET to "Apply knowledge and skills in {course_title.lower()} to meet organizational and industry requirements."
    ELSE:
        SET to ""
```

## Empty Value Detection

The system treats the following as empty values:
- `None`
- `""`
- `"null"`
- `"None"`

```python
def is_empty(val):
    return val is None or val == "" or val == "null" or val == "None"
```
