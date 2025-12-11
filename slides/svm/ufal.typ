// ÚFAL Polylux Theme
// Inspired by the ÚFAL Marp theme and Touying theme
// Built with Polylux framework

#import "@preview/polylux:0.4.0": *
#import "@preview/polylux:0.4.0": slide as polylux-slide

// ===== COLORS =====
#let ufal-orange = rgb("#f47b20")
#let ufal-gray = rgb("#EFEFEF")
#let text-color = rgb("#252525")
#let muted-color = rgb("#888888")

// ===== FONTS =====
#let font-sans = ("Fira Sans", "Liberation Sans", "Arial")
#let font-mono = ("Consolas", "Liberation Mono")

// ===== LOGOS =====
#let ufal-logo = image("img/ufal.svg", width: 1.2cm)
#let ufal-logo-title = image("img/ufal.svg", width: 1.6cm)
#let cuni-logo = image("img/cuni.svg", width: 4.5cm)
#let langtech-logo = image("img/langtech.svg", width: 1.8cm)
#let opvv-logo = image("img/opvv.svg", width: 2.2cm)
#let cc-by-sa-logo = image("img/by-sa.svg", width: 2.7cm)
#let cc-by-nc-sa-logo = image("img/by-nc-sa.eu.svg", width: 2.7cm)

// ===== SHARED COMPONENTS =====

/// Creates a sections band showing all sections with current section highlighted
/// Returns empty content if no sections are registered
#let sections-band = toolbox.all-sections((sections, current) => {
  if sections.len() == 0 {
    []
  } else {
    // Neutralize all link styling within the sections band
    show link: it => it.body
    set text(size: 10pt, font: font-sans)
    sections
      .map(s => if s == current {
        text(fill: rgb("#3e3e3e"), weight: "regular")[#s]
      } else {
        text(fill: muted-color, weight: "regular")[#s]
      })
      .join(text(fill: muted-color)[ #h(5pt) • #h(5pt) ])
  }
})

/// Creates an animated outline of all registered sections
/// Each section appears as a numbered box with orange styling
/// Returns empty content if no sections are registered
#let outline = toolbox.all-sections((sections, current) => {
  if sections.len() == 0 {
    []
  } else {
    show link: it => it.body
    stack(
      dir: ttb,
      spacing: 0.8em,
      ..sections
        .enumerate()
        .map(((i, section)) => {
          block(
            width: 100%,
            // inset: (left: 1.2em, right: 0.8em, top: 0.8em, bottom: 0.8em),
            // radius: 4pt,
            // fill: ufal-gray,
            // stroke: (left: (paint: ufal-orange, thickness: 6pt)),
          )[
            #stack(
              dir: ltr,
              spacing: 0.5em,
              text(
                size: 1.1em,
                // weight: "semibold",
                fill: text-color,
                font: font-sans,
              )[#(i + 1).],
              text(
                size: 1.1em,
                // weight: "semibold",
                fill: text-color,
                font: font-sans,
              )[#section],
            )
          ]
        }),
    )
  }
})

/// Creates the UFAL header bar with title and logo
/// Default settings are optimized for title slides
#let ufal-header-bar(
  title-text: none,
  title-size: 25pt,
  left-padding: 0.3cm,
  top-padding: 0.25cm,
  width: 100%,
  dx: 0cm,
) = {
  place(
    top + left,
    dx: dx,
    rect(
      width: width,
      height: 1.6cm,
      fill: ufal-gray,
      stroke: none,
    )[
      #stack(
        dir: ltr,
        spacing: 1fr,
        align(center + horizon)[
          #if title-text != none [
            #text(
              fill: ufal-orange,
              size: title-size,
              weight: "bold",
              font: font-sans,
            )[#title-text]
          ]
        ],
        align(center + horizon)[
          #ufal-logo
        ],
      )
    ],
  )
}

// ===== THEME SETUP =====
#let ufal-theme(
  footer-content: "ÚFAL slides template",
  body,
) = {
  // Basic text styling
  set text(
    font: font-sans,
    size: 20pt,
    fill: text-color,
  )

  set par(
    leading: 1em,
    justify: false,
  )

  // Heading styles
  set heading(numbering: none)

  // Hide level-1 headings as they are used for slide titles
  show heading.where(level: 1): none

  show heading.where(level: 2): it => {
    v(0.4em)
    set text(
      size: 1.3em,
      weight: "bold",
    )
    it
    v(0.3em)
  }

  show heading.where(level: 3): it => {
    v(0.3em)
    set text(
      size: 1.2em,
      weight: "bold",
    )
    it
    v(0.2em)
  }

  show heading.where(level: 4): it => {
    v(0.3em)
    set text(
      size: 1em,
      weight: "bold",
    )
    it
    v(0.1em)
  }

  // Inline code: 1.3em makes Consolas approximately the same size as Fira Sans
  show raw.where(block: false): set text(
    font: font-mono,
    size: 1.3em,
    fill: text-color,
  )

  // Block code: 1em for better readability in code blocks
  show raw.where(block: true): set text(
    font: font-mono,
    size: 1em,
    fill: text-color,
  )

  // Use custom tmTheme for syntax highlighting
  set raw(
    theme: "ufal-syntax.tmTheme",
  )

  show raw.where(block: true): block.with(
    fill: rgb("#eeeeee"),
    inset: 0.5em,
    radius: 3pt,
    width: 100%,
  )

  // Link styling
  show link: it => {
    set text(fill: ufal-orange)
    underline(it, stroke: 2pt, offset: 0.2em)
  }

  show hide: it => {
    set list(marker: none)
    set enum(numbering: n => none)

    it
  }

  show quote: it => {
    block(
      width: 100%,
      inset: (left: 1.0em, right: 0.8em, top: 0.5em, bottom: 0.5em),
      radius: 0pt,
      stroke: (left: (paint: ufal-orange, thickness: 6pt)),
    )[
      #set text(size: 0.9em, fill: rgb("#3c3c3c"))
      #it.body

      // Show attribution if present
      #if it.attribution != none [
        #align(right)[
          #text(size: 0.8em, style: "italic", fill: muted-color)[
            — #it.attribution
          ]
        ]
      ]
    ]
  }

  // Enhanced list spacing
  show list: it => {
    it
    v(0.2em) // Additional space after each list
  }

  // Custom bullets
  set list(marker: (text(size: 1em)[●], text(size: 1em)[○], text(size: 0.7em)[□]))

  // Table styling
  show table: set text(size: 1em)
  show table: set table(inset: 0.5em)

  // Page setup with header and footer
  set page(
    paper: "presentation-16-9",
    margin: (top: 2.5cm, bottom: 1.3cm, left: 1.2cm, right: 1.2cm),
    header: [
      #set align(left + top)
      #toolbox.next-heading(h => ufal-header-bar(
        title-text: h,
        title-size: 25pt,
        left-padding: 0.1cm,
        top-padding: 0.5cm,
        width: 100% + 2.4cm,
        dx: -1.2cm,
      ))
      #v(-0.5cm)
    ],
    footer: [
      #set align(left + bottom)

      // Only show footer if content is provided and not empty
      #if footer-content != none and footer-content != "" [
        #context [
          #let footer-text = text(
            fill: rgb("#ffffff"),
            size: 12pt,
            weight: "bold",
            font: font-sans,
          )[#footer-content]

          // Measure the text width and add some padding, with a minimum width
          #let text-width = measure(footer-text).width
          #let footer-width = calc.max(text-width + 0.8cm, 7cm)

          #place(
            bottom + left,
            dx: -1.2cm,
            dy: 0cm,
            rect(
              width: footer-width,
              height: 0.7cm,
              fill: ufal-orange,
              stroke: none,
            )[
              #align(left + horizon)[
                #pad(left: 0.3cm)[
                  #footer-text
                ]
              ]
            ],
          )
        ]
      ]

      // Sections band (left-aligned with footer bar)
      #if footer-content != none and footer-content != "" [
        #context [
          #let footer-text = text(
            fill: rgb("#ffffff"),
            size: 12pt,
            weight: "bold",
            font: font-sans,
          )[#footer-content]

          // Calculate footer width to position sections band
          #let text-width = measure(footer-text).width
          #let footer-width = calc.max(text-width + 0.8cm, 7cm)

          #place(
            bottom + left,
            dx: -1.2cm + footer-width + 0.5cm,
            dy: -0.2cm,
            sections-band,
          )
        ]
      ] else [
        // If no footer content, position at left with small padding
        #place(
          bottom + left,
          dx: 0.3cm,
          dy: -0.2cm,
          sections-band,
        )
      ]

      // Pagination
      #place(
        bottom + right,
        dx: 0.9cm,
        dy: -0.2cm,
        text(
          fill: text-color,
          size: 12pt,
          font: font-sans,
        )[#toolbox.slide-number/#toolbox.last-slide-number],
      )
    ],
  )

  body
}

// ===== SLIDE FUNCTIONS =====

// Override the default slide function
#let slide(body) = {
  polylux-slide[
    #body
  ]
}

// Title slide
#let title-slide(
  title: none,
  name: none,
  subtitle: none,
  author: none,
  date: none,
  institution: [
    Charles University\
    Faculty of Mathematics and Physics\
    Institute of Formal and Applied Linguistics
  ],
  license-type: none,
  langtech: false,
  body,
) = slide[
  #set page(header: none, footer: none, margin: 0cm)

  // Header with title
  #ufal-header-bar(title-text: title)

  // Main content - use columns if body content is provided
  #pad(top: 3.65cm, left: 1.2cm, right: 1.2cm)[
    #if body != [] and body != none [
      // Two-column layout when body content is provided
      #grid(
        columns: (1fr, 1fr),
        column-gutter: 2em,
        // Left column: title information
        [
          #if name != none [
            #text(
              size: 38pt,
              weight: "bold",
              fill: ufal-orange,
            )[#name]
            #v(-0.5cm)
          ]

          #if subtitle != none [
            #text(size: 25pt)[#subtitle]
            #v(0.5cm)
          ]

          // Author and date in left column (maintain original spacing)
          #if author != none [
            #v(1.8cm)
            #text(size: 22pt, weight: "semibold")[#author]
          ]

          #if date != none [
            #rect(
              fill: ufal-gray,
              inset: (x: 0.5em, y: 0.5em),
              radius: 0.5em,
            )[
              #stack(
                dir: ltr,
                spacing: 0.5em,
                image("img/calendar.svg", height: 0.7em),
                text(size: 18pt)[#date],
              )
            ]
          ]
        ],
        // Right column: body content
        [
          #body
        ],
      )
    ] else [
      // Original single-column layout when no body content
      #if name != none [
        #text(
          size: 38pt,
          weight: "bold",
          fill: ufal-orange,
        )[#name]
        #v(-0.5cm)
      ]

      #if subtitle != none [
        #text(size: 25pt)[#subtitle]
        #v(0.5cm)
      ]

      // Author and date
      #place(
        bottom,
        dy: 5.5cm,
      )[
        #if author != none [
          #text(size: 22pt, weight: "semibold")[#author]
        ]

        #if date != none [
          #rect(
            fill: ufal-gray,
            inset: (x: 0.5em, y: 0.5em),
            radius: 0.5em,
          )[
            #stack(
              dir: ltr,
              spacing: 0.5em,
              image("img/calendar.svg", height: 0.7em),
              text(size: 18pt)[#date],
            )
          ]
        ]
      ]
    ]
  ]

  // Footer with logos
  #place(
    bottom + left,
    rect(
      width: 100%,
      height: 2.2cm,
      fill: ufal-gray,
      stroke: none,
    )[
      #place(
        left + horizon,
        dx: 0.15cm,
        stack(
          dir: ltr,
          cuni-logo,
          ufal-logo-title,
        ),
      )

      #place(
        left + horizon,
        dx: 15.5cm,
        text(size: 10pt)[
          #set par(leading: 0.8em)
          #institution
        ],
      )

      #if langtech [
        #place(
          left + horizon,
          dx: 7cm,
          stack(
            dir: ltr,
            spacing: 0.8cm,
            langtech-logo,
            opvv-logo,
          ),
        )
      ]

      // License
      #if license-type == "cc-by-sa" [
        #place(
          right + horizon,
          dx: -1.5cm,
          stack(
            dir: ttb,
            spacing: 0.2cm,
            align(center)[#cc-by-sa-logo],
            align(center)[
              #text(size: 9pt)[unless otherwise stated]
            ],
          ),
        )
      ] else if license-type == "cc-by-nc-sa" [
        #place(
          right + horizon,
          dx: -1.5cm,
          stack(
            dir: ttb,
            spacing: 0.2cm,
            align(center)[#cc-by-nc-sa-logo],
            align(center)[
              #text(size: 9pt)[unless otherwise stated]
            ],
          ),
        )
      ]
    ],
  )
]

// Summary slide
#let summary-slide(
  title: none,
  subtitle: none,
  link: none,
  body,
) = slide[
  #set page(header: none, footer: none, margin: 0cm, fill: ufal-gray)
  #set align(center + horizon)

  // White content rectangle with title and subtitle positioned relative to it
  #place(center + horizon, dy: 0cm)[
    #stack(
      dir: ttb,
      spacing: 1cm,
      // Title and subtitle above the rectangle
      {
        stack(
          dir: ttb,
          spacing: 0.5cm,
          // Subtitle box
          if subtitle != none {
            rect(
              fill: ufal-orange,
              inset: (x: 2.5cm, y: 0.3cm),
              radius: 0pt,
            )[
              #align(center)[
                #text(
                  fill: rgb("#ffffff"),
                  size: 14pt,
                  weight: "bold",
                  font: font-sans,
                )[#subtitle]
              ]
            ]
          },
          v(30pt),
          // Main title
          if title != none {
            text(
              size: 28pt,
              weight: "bold",
              fill: ufal-orange,
              font: font-sans,
            )[#title]
          },
        )
      },
      // White content rectangle
      rect(
        width: 24cm,
        fill: rgb("#ffffff"),
        stroke: 0.15cm + ufal-orange,
        inset: (x: 1cm, y: 1cm),
        radius: 0pt,
      )[
        #set align(left)
        #body
      ],
      // Link positioned below the rectangle
      if link != none {
        text(
          size: 18pt,
          weight: "semibold",
          fill: ufal-orange,
          font: font-mono,
        )[#link]
      },
    )
  ]
]

// Part slide (section divider)
#let section-slide(section: none, body) = slide[
  #set page(header: none, footer: none, margin: 0pt, fill: ufal-gray)
  #set align(center + horizon)

  #if section != none [
    #toolbox.register-section[#section]
  ]

  #rect(
    width: 20cm,
    fill: ufal-orange,
    radius: 0pt,
    inset: (x: 1cm, y: 0.8cm),
  )[
    #align(center + horizon)[
      #text(
        fill: rgb("#ffffff"),
        size: 25pt,
        weight: "bold",
        font: font-sans,
      )[#body]
    ]
  ]
]

// Blank slide (no header, no footer, custom margin)
#let blank-slide(body) = slide[
  #set page(header: none, footer: none, margin: 1.2cm)
  #body
]

// ===== HELPER FUNCTIONS =====


#let bordered-box(img, padding: 0pt) = {
  block(
    stroke: 1pt + rgb("#828282"),
    inset: padding,
    radius: 0pt,
  )[
    #img
  ]
}
#let inline-image(path) = box(image(path, height: 01em), baseline: 10%, inset: (right: 0.2em))

// Info box with customizable heading and content
#let infobox(title: none, icon: none, fill: none, body) = {
  let title-text = if icon != none { [#icon #h(0.1em) #title] } else { title }
  let fill = if fill == none {ufal-orange} else {fill}
  block(
    width: 100%,
    inset: (left: 1.2em, right: 0.8em, top: 0.8em, bottom: 0.8em),
    radius: 4pt,
    fill: fill.lighten(95%),
    stroke: (left: (paint: fill, thickness: 6pt)),
  )[
    #if title != none [
      #text(weight: "bold", fill: fill)[#title-text]
      #v(-0.1em)
    ]
    #body
  ]
}

// Vertically center content using flexible spacing
#let halign(body) = {
  v(1fr)
  body
  v(1fr)
}

// Source link - small, right-aligned link for referencing sources
#let source(url, title: none) = {
  let link-text = if title != none { "source: " + title } else { "source: " + url }

  align(
    right,
    text(
      size: 12pt,
      fill: muted-color,
      font: font-sans,
    )[
      #link(url)[#link-text]
    ],
  )
}

// Source slide - positions source link in top-right corner of slide
#let source-slide(url, title: none) = {
  let link-text = if title != none { "source: " + title } else { "source: " + url }

  place(
    top + right,
    dx: -1.2cm,
    dy: -1.85cm,
    text(
      size: 12pt,
      fill: muted-color,
      font: font-sans,
    )[
      #link(url)[#link-text]
    ],
  )
}

// Todo box - styled placeholder for unfinished content
#let todo(content) = {
  block(
    width: 100%,
    inset: (left: 1.2em, right: 0.8em, top: 0.8em, bottom: 0.8em),
    radius: 4pt,
    fill: ufal-gray,
    stroke: (left: (paint: ufal-orange, thickness: 6pt)),
  )[
    #text(weight: "bold", fill: ufal-orange)[TODO]
    #v(-0.1em)
    #text(fill: text-color)[#content]
  ]
}
