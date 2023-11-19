# i18n-json-spreadsheet

Lazy i18n json to spreadsheet and back tool. 

The aim of this utility is to help the management of JSON translations 
file used for example in JS frontends to handle locales.

Usually we can have key/value items nested in some way like the following:

```json
{
  "hello": "ciao",
  "how_are_you": "come stai",
  "component_a": {
    "my_name_is": "il mio nome é"
  }
}
```

To avoid editors to edit JSON files directly, ofted in git repos, the idea is 
to create/update online spreadsheet on Google Docs and maybe Microsoft Office 365.

## Installation

### PIP 

The package is available on [Pypi](https://pypi.org/project/i18nconverter/). To install locally on a virtual env or globally execute a standard package installation: 

```bash
❯ pip install i18nconverter
```

## Authentication

At the moment we support only Service Account file to authenticate API for Google Drive and Google Spreadsheet. To get you SA file you have to:

- Visit [Google Developers Console](https://console.developers.google.com/) to create a new project
- In the input box "Search for APIs and Services" search for _Google Drive API_ and check it.
- Repeat for _Google Sheets API_
- Create and download the key file following https://cloud.google.com/iam/docs/keys-create-delete 

## Quickstart

1. Move to your current project directory and configure the environment

```bash
❯ i18nconverter init
📝 Creating local configuration...
↳ GCP Service Account JSON file location? : /tmp/my-sa-file.json
↳ Google Spreadsheet link? : NA
↳ How do you manage locale codes?
   ↳ [1] in different files
   ↳ [2] on the first level of JSON
 [1]:

🎉  Configuration file created .i18nconverter.json 
```

Since we're going to create a new file we can insert a random string to _Google Spreadsheet link?_ question.

2. Then we can create the new spreadsheet where manage translations

```bash
❯ i18nconverter create --name "MY_PROJECT_Translations" --owner "john.doe@none.com" --save
📝 Creating new spreadsheet "MY_PROJECT_Translations"...
https://docs.google.com/spreadsheets/d/99999-8
✅ Config file updated.
```

3. Create entries to the previously created Google Spreadsheet for italian using dedicated sheet named `it-IT`. 

```bash
 ❯ i18nconverter togdoc -i public/locales/it-IT/translation.json --sheet IT --create-sheet
✅ Update completed.
💻 Check at https://docs.google.com/spreadsheets/d/99999-8
```

Then repeat for `en-US` locale.

```bash
❯ i18nconverter togdoc -i public/locales/en-US/translation.json --sheet en-US --create-sheet
✅ Update completed.
💻 Check at https://docs.google.com/spreadsheets/d/99999-8
```

4. Fill some translations on Google Docs
5. Update local JSON file 

```bash
❯ i18nconverter tojson -o public/locales/it-IT/translation.json -s it-IT
```

6. Check differences locally maybe with the help of `git diff`

## How to

This tool is intended to be used as CLI tool. 

### Get help

```bash
❯ i18nconverter --help
Usage: i18nconverter [OPTIONS] COMMAND [ARGS]...

Options:
  --auth TEXT  Service Account JSON file path
  --silent     Silent mode: questions to user will be skipped (ignored for
               setup)
  --help       Show this message and exit.

Commands:
  init
  togdoc
  tojson
  tokv
```

### Create local permantent config file

To simplify the frequent usage we support a local configuration file that will be searched *only in the current directory*.

```bash
 ❯ i18nconverter init
📝 Creating local configuration...
↳ GCP Service Account JSON file location? : /tmp/my-sa-file.json
↳ Google Spreadsheet link? : https://docs.google.com/spreadsheets/d/ffa9a9f99f
↳ How do you manage locale codes?
   ↳ [1] in different files
   ↳ [2] on the first level of JSON
 [1]: 1


🎉  Configuration file created .i18nconverter.json
```

As you can see a file in the same directory called `.i18nconverter.json` will be created and you can skip setting SA file path and source/target spreadsheet link on each command.

### Json To Google Spreadsheet

```bash
❯ i18nconverter togdoc --help
Usage: i18nconverter togdoc [OPTIONS]

Options:
  -i, --infile TEXT               JSON input file
  -ol, --outlink TEXT             Destination link for Google Spreadsheet
  -s, --sheet TEXT                Destination sheet in Google Spreadsheet
  -o, --overwrite                 Clear worksheet before writing values
  --create-sheet / --no-create-sheet
                                  Create new sheet with given name if it not
                                  exists
  --help                          Show this message and exit.
```

### Google Spreadsheet to Json file

```bash
❯ i18nconverter tojson --help
Usage: i18nconverter tojson [OPTIONS]

Options:
  -o, --outfile TEXT  JSON output file
  -il, --inlink TEXT  Source link for Google Spreadsheet
  --start-cell TEXT   Start reading from this cell coordinates
  -s, --sheet TEXT    Source sheet in Google Spreadsheet
  --help              Show this message and exit.
```

### Compare Json file and Google Spreadsheet

```bash
❯ i18nconverter compare --help
Usage: i18nconverter compare [OPTIONS]

Options:
  -f, --file TEXT       JSON file for comparison  [required]
  -l, --link TEXT       Link to Google Spreadsheet
  -s, --sheet TEXT      Source sheet in Google Spreadsheet
  -c, --column INTEGER  Colum to read in Google Spreadsheet
  --help                Show this message and exit.
```

The response will show two csv with differences:

```bash
❯ i18nconverter compare -f /tmp/somefile.json
Keys present in Google Spreadsheet and not present in JSON: 
actions.addedaaa
Keys present in JSON and not present in Google Spreadsheet: 
actions.added
```