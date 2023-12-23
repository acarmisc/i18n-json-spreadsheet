import gspread
from gspread.exceptions import WorksheetNotFound

from i18nconverter.utils.gspreadsheet_to_json import GspreadToJson
from i18nconverter.utils.json_to_kv import JsonToKv


class KvToGspread:

    def __init__(self, sa_file: str) -> None:
        self.sa_file = sa_file

    def update_spreadsheet(self, infile: str, file_url: str, start_cell: str = 'A1',
                           sheet: str = 'Sheet1', merge: bool = False, create_sheet: bool = False,
                           overwrite: bool = False):
        gc = gspread.service_account(filename=self.sa_file)
        spreadsheet = gc.open_by_url(file_url)

        try:
            sh = spreadsheet.worksheet(sheet)
        except WorksheetNotFound as e:
            if create_sheet:
                sh = spreadsheet.add_worksheet(sheet, rows=2, cols=2)
            else:
                raise Exception(f'Unable to use Worksheet {sheet}')

        if overwrite:
            sh.clear()
            return

        # merge existing with new values
        jkvf = JsonToKv(from_file=infile)
        reader = GspreadToJson(self.sa_file, file_url, sheet, start_cell)
        existing = reader.read_flat()
        flat_json = jkvf.flatten_json()

        to_write = flat_json | existing

        jkv = JsonToKv(from_dict=to_write)
        sh.update(start_cell, jkv.as_kvlist())
