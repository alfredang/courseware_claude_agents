# Slide Template Format

## Purpose

Documents the branding and formatting requirements for generated presentation slides based on the `slide_template.pptx` template.

## Template File

`.skills/generate_slides/templates/slide_template.pptx` - Standard WSQ course presentation template

## Branding Requirements

### Background
- **Color**: White background throughout all slides

### Standard Pages
- **Front Page**: Standard title slide with course branding
- **Back Page**: Standard closing slide with organization details

## Content Placeholders

The following elements are dynamically replaced from the Course Proposal:

| Placeholder | Source | Description |
|-------------|--------|-------------|
| Learning Outcomes | Course Proposal | LO statements for each Learning Unit |
| Skills Framework K | Course Proposal | Knowledge (K) factors from TSC |
| Skills Framework A | Course Proposal | Ability (A) factors from TSC |
| TSC Ref Code | Course Proposal | Technical Skills Competency reference code |
| Lesson Plan | Course Proposal | Lesson structure and topics |

## Typography

### Page Header
| Property | Value |
|----------|-------|
| Font Family | Arial |
| Font Size | 36 point |
| Style | Bold (recommended) |

### Page Body
| Property | Value |
|----------|-------|
| Font Family | Arial |
| Font Size | 24 point |
| Line Spacing | Single spacing |

## Slide Structure

### Front Page (Title Slide)
```
┌─────────────────────────────────────┐
│                                     │
│     [Organization Logo]             │
│                                     │
│     Course Title (Arial 36pt)       │
│                                     │
│     TSC Ref Code                    │
│     Skills Framework Name           │
│                                     │
└─────────────────────────────────────┘
```

### Content Slides
```
┌─────────────────────────────────────┐
│ Section Title (Arial 36pt)          │
├─────────────────────────────────────┤
│                                     │
│ • Bullet point 1 (Arial 24pt)       │
│ • Bullet point 2                    │
│ • Bullet point 3                    │
│                                     │
│ [Speaker Notes Area]                │
└─────────────────────────────────────┘
```

### Learning Outcome Slides
```
┌─────────────────────────────────────┐
│ Learning Outcomes (Arial 36pt)      │
├─────────────────────────────────────┤
│                                     │
│ LO1: [Description] (Arial 24pt)     │
│                                     │
│ LO2: [Description]                  │
│                                     │
│ LO3: [Description]                  │
│                                     │
└─────────────────────────────────────┘
```

### Skills Framework Slides
```
┌─────────────────────────────────────┐
│ Skills Framework (Arial 36pt)       │
├─────────────────────────────────────┤
│                                     │
│ Knowledge (K):                      │
│ K1: [Description] (Arial 24pt)      │
│ K2: [Description]                   │
│                                     │
│ Abilities (A):                      │
│ A1: [Description]                   │
│ A2: [Description]                   │
│                                     │
└─────────────────────────────────────┘
```

### Back Page (Closing Slide)
```
┌─────────────────────────────────────┐
│                                     │
│     Thank You                       │
│                                     │
│     [Organization Name]             │
│     [Contact Information]           │
│                                     │
│     [Organization Logo]             │
│                                     │
└─────────────────────────────────────┘
```

## Data Mapping from Course Proposal

| Slide Element | CP Field |
|---------------|----------|
| Course Title | `Course_Title` |
| TSC Ref Code | `TSC_Code` |
| Skills Framework | `Skills_Framework` / `TSC_Sector_Abbr` |
| Learning Outcomes | `Learning_Units[].LO` |
| K Factors | `Learning_Units[].K_numbering_description` |
| A Factors | `Learning_Units[].A_numbering_description` |
| Topics | `Learning_Units[].Topics[].Topic_Title` |
| Lesson Plan | `Learning_Units[].Topics[].Bullet_Points` |

## Style Guidelines

1. **Consistency**: Maintain consistent font sizes throughout
2. **Readability**: Use single spacing for body text clarity
3. **White Space**: Ensure adequate margins and padding
4. **Branding**: Keep white background for professional appearance
5. **Accessibility**: Arial font ensures readability across devices
