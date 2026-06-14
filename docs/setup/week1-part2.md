Questions and Answers

This document explains the basic concepts of Bootstrap, Flask Routing, Template Inheritance, base.html, and reusable templates in simple words.

1. What is Bootstrap?

Answer: Bootstrap is a front-end framework used to design web pages quickly. It gives ready-made CSS classes for buttons, forms, navigation bars, cards, tables, grids, and responsive layouts.

Instead of writing all the CSS from the beginning, Bootstrap helps us create clean and mobile-friendly web pages faster.

2. What is Flask Routing?

Answer: Flask routing is the method used to connect a URL with a Python function. When a user opens a particular URL in the browser, Flask checks the route and runs the matching function.

For example, / can show the home page, while /login can show the login page.

3. What is Template Inheritance?

Answer: Template inheritance means reusing one common HTML layout for many pages. Instead of writing the same navbar, footer, CSS links, and common structure in every HTML file, we create one main template and extend it in other pages.

This keeps the project clean and avoids repeated code.

4. What is base.html?

Answer: base.html is the main layout file in a Flask project. It normally contains the common structure of the website, such as HTML tags, Bootstrap links, navbar, footer, JavaScript links, and content blocks.

Other pages can extend base.html and place their page-specific content inside the defined block.

5. Why reusable templates matter?

Answer: Reusable templates are important because they reduce repeated code and make the application easier to maintain.

When we need to change the navbar, we update it only once, and the change reflects across all pages. This saves time, reduces mistakes, and keeps the design consistent.
