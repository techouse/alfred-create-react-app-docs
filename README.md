# Create React App Docs Workflow for Alfred

![GitHub release](https://img.shields.io/github/release/techouse/alfred-create-react-app-docs.svg)
![GitHub All Releases](https://img.shields.io/github/downloads/techouse/alfred-create-react-app-docs/total.svg)
![GitHub](https://img.shields.io/github/license/techouse/alfred-create-react-app-docs.svg)


Search the [Create React App documentation](https://create-react-app.dev/docs/getting-started) using [Alfred](https://www.alfredapp.com/).

![demo](demo.gif)

## Installation

1. [Download the latest version](https://github.com/techouse/alfred-create-react-app-docs/releases/latest)
2. Install the workflow by double-clicking the `.alfredworkflow` file
3. You can add the workflow to a category, then click "Import" to finish importing. You'll now see the workflow listed in the left sidebar of your Workflows preferences pane.

## Usage

Just type `cra` followed by your search query.

```
cra css modules
```

Either press `⌘Y` to Quick Look the result, or press `<enter>` to open it in your web browser.

### Note

Built using [Alfred-Workflow](https://github.com/deanishe/alfred-workflow).
The lightning fast search is powered by [Algolia](https://www.algolia.com) using the _same_ index as the official [Create React App](https://create-react-app.dev/docs/getting-started) website.