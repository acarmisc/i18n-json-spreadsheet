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

## How to

This tool is intended to be used as CLI tool. 


### Get Help

```bash
❯ i18nconverter --help
Usage: i18nconverter [OPTIONS] COMMAND [ARGS]...

Options:
  --auth TEXT  Service Account JSON file path
  --silent     Silent mode: questions to user will be skipped (ignored for
               setup)
  --help       Show this message and exit.

Commands:
  setup
  togdoc
  tojson
  tokv
```

### Create local permantent config file

To simplify the frequent usage we support a local configuration file that will be searched *only in the current directory*.

```bash
 ❯ i18nconverter setup
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

