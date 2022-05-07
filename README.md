# DWS transaction overview to parqet activities-csv-file

`dws-to-parqet.py` is a simple script to turn the transaction overview of an [DWS](https://www.dws.de/) account into an importable CSV for [parqet](https://www.parqet.com/)s activities.  
  
## 🛠️ Requirements

You need to have Python Version 3 installed. Get it [here](https://www.python.org/downloads/).  
It may work under Python Version 2 as well, but I have not checked any compatibility.

## 💻 Usage

Run the script using

```bash
py dws-to-parqet.py
```

It has the following arguments:

| Argument | description |
|----------|-------------|
| `--help`, `-h` | shows a help with the available arguments |
| `--input`, `-i` | the input-file (CSV) which should be transformed (required) |
| `--output`, `-o` | the output-file (CSV) to store the transformed data (required) |

The output-file can then be used via the [CSV-activity-importer](https://www.parqet.com/blog/csv) on [parqet](https://www.parqet.com/).
