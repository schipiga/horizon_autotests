from selenium.webdriver.common.by import By

from .base import Block


class Row(Block):
    pass


class Table(Block):

    Row = Row
    row_tag = "tr"
    cell_tag = "td"
    columns = None

    def row(self, **kwgs):
        row = self.Row(By.XPATH, self._row_selector(**kwgs))
        row.set_container(self)
        return row

    def _row_selector(self, **kwgs):
        pos_tmpl = '[position()={} and contains(., "{}")]'
        cell_selectors = []
        for name, value in kwgs.items():
            position = self.columns[name]
            cell_selectors.append(
                self.cell_tag + pos_tmpl.format(position, value))

        return '//{}[{}]'.format(self.row_tag, " and ".join(cell_selectors))
